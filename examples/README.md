Example images (from validation set) from different stages in the prediction.\n
103.png is the image used for prediciton 512x512x3 from the downscaled center 1080x1080x3 of a 1920x1080x3\n
103t.png is the target for the image, hand labeled.\n
103pred.png is the prediction from the neural network\n
103predThresh.png is the prediciton thresholded using .6 (this value was explored in the thesis)\n
103edgePrediction.png is the original image with the corners overlayed. These corners are for a concave quadrilateral estimation of the runway.\n
The corner values are used in the altitude estimation of the drone using the width of the runway as a known dimension.\n
Two different methods are developed in the thesis.\n
The first is based on the two closest corners that define the width (IE true corners of the ruwnay and not just points on the edge)\n
The second is based on four points, with two along each lengthwise edge of the runway. \n
  These four points do not need to be corners, but the further the points are away and the more closely they follow the runway edge, the more accurate the prediction.

