from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, concatenate, SpatialDropout2D, Conv2DTranspose
from tensorflow.keras.models import Model

# This is the U-Net model used for final predictions for thesis.

# U-Net convolution block with spatial dropout
# INPUTS:
#   filters: filter count for convolutions
#   kernels: kernel size of conv
#   input_layer: prev layer to attatch block to
#   layer_num: layer number for naming, String or char
# OUTPUTS:
#   Keras layer output
def unetConvBlock(filters, kernel, input_layer, layer_num=''):
    if layer_num:
        x = Conv2D(filters, kernel, activation='relu', padding='same', kernel_initializer='he_normal', name='l' + layer_num + "conv1")(
            input_layer)
        x = SpatialDropout2D(.2)(x)
        x = Conv2D(filters, kernel, activation='relu', padding='same', kernel_initializer='he_normal', name='l' + layer_num + "conv2")(x)

        return x
    else:
        x = Conv2D(filters, kernel, activation='relu', padding='same', kernel_initializer='he_normal')(input_layer)
        x = SpatialDropout2D(.2)(x)
        x = Conv2D(filters, kernel, activation='relu', padding='same', kernel_initializer='he_normal')(x)

        return x



# Modified U-Net Model
# INPUTS:
#   filters: Intitial filter count for model, determines all layer filter counts
#   input_size: size of input image, images used in thesis are 512x512x3
# OUTPUTS:
#   Keras model
# Modifications to original U-Net Structure
#   transposed convolution instead of upsampling
def unet(filters=64, input_size=(512, 512, 3)):

    inputs = Input(input_size)

    x = unetConvBlock(filters, 3, inputs, '1')
    l1Out = x

    x = MaxPooling2D(pool_size=(2, 2), name='pool1')(x)

    x = unetConvBlock(filters * 2, 3, x, '2')
    l2Out = x

    x = MaxPooling2D(pool_size=(2, 2), name='pool2')(x)

    x = unetConvBlock(filters * 4, 3, x, '3')
    l3Out = x

    x = MaxPooling2D(pool_size=(2, 2), name='pool3')(x)

    x = unetConvBlock(filters * 8, 3, x, '4')
    l4Out = x

    x = MaxPooling2D(pool_size=(2, 2), name='pool4')(x)

    x = unetConvBlock(filters * 16, 3, x, '5')

    x = Conv2DTranspose(filters * 8, (2, 2), strides=(2, 2), padding='same')(x)
    x = concatenate([l4Out, x], axis=3)

    x = unetConvBlock(filters * 8, 3, x, '6')

    x = Conv2DTranspose(filters * 4, (2, 2), strides=(2, 2), padding='same')(x)
    x = concatenate([l3Out, x], axis=3)

    x = unetConvBlock(filters * 4, 3, x, '7')

    x = Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(x)
    x = concatenate([l2Out, x], axis=3)

    x = unetConvBlock(filters * 2, 3, x, '8')

    x = Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(x)
    x = concatenate([l1Out, x], axis=3)

    x = unetConvBlock(filters, 3, x, '9')

    x = Conv2D(1, (1, 1), activation='sigmoid', padding='same', kernel_initializer='he_normal')(x)

    model = Model(inputs, x)
    return model

