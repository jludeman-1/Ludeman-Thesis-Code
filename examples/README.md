Example images (from validation set) from different stages in the prediction.\
103.png is the image used for prediciton 512x512x3 from the downscaled center 1080x1080x3 of a 1920x1080x3\
103t.png is the target for the image, hand labeled.\
103pred.png is the prediction from the neural network\
103predThresh.png is the prediciton thresholded using .6 (this value was explored in the thesis)\
103edgePrediction.png is the original image with the corners overlayed. These corners are for a concave quadrilateral estimation of the runway.\
The corner values are used in the altitude estimation of the drone using the width of the runway as a known dimension.\
Two different methods are developed in the thesis.\
The first is based on the two closest corners that define the width (IE true corners of the ruwnay and not just points on the edge)\
The second is based on four points, with two along each lengthwise edge of the runway. \
  These four points do not need to be corners, but the further the points are away and the more closely they follow the runway edge, the more accurate the prediction.

