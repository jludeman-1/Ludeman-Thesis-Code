from models import unet
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

model = unet(16)
model.summary()

model.load_weights("./pretrained_models/unet_16.h5")

predArr = np.zeros([1,512,512,3])
predArr[0] = np.array(Image.open("./images/1.png").resize((512, 512))) / 255

pred = model.predict(predArr)

# Simple threshold
thresh = pred[0] >= .6

target = np.array(Image.open("./target/1.png").resize((512, 512))) / 255

# Needs to be reshaped from [512,512] to [512,512,1]
diff = thresh != target.reshape([512,512,1])


plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.axis('off')
plt.title("Prediction Image")
plt.imshow(thresh, cmap='gray')

plt.subplot(1, 2, 2)
plt.axis('off')
plt.title("Difference From Target")
plt.imshow(diff, cmap='gray')

plt.show()


