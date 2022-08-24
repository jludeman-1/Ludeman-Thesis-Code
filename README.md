# Ludeman-Thesis-Code

Abstract


Runway Location for Autonomous Aircraft Using Neural Networks and Computer Vision\

John Ludeman, M.S.

University of Nebraska, 2022

Advisor: Dr. Qiuming Zhu



Recent advancements in neural network architecture coupled with increased graphics card processing power have allowed for the rise of real-time prediction. Proposed is a method of using a semantic segmentation neural network followed by computer vision methods and lens equations to recover the location of a runway and the altitude of a drone from an image and a known runway dimension. The best performing neural network model had an intersect over union accuracy of 95.5% with an inference speed of 12.5 frames per second. The final error in predicted altitude using the best of two developed methods was less than 15% on average, with a peak error of 23.5%. 
\



Final error results of code. Run on video feeds the neural network has not been trained on. The video feeds were taken from the drone holding 20ft and 140ft while moving. The x axis is a frame from video feed, taken once every second. Program runs at ~12FPS but to increase variety of the video feed, only a frame every second was used.

![test20ft](https://github.com/jludeman-1/Ludeman-Thesis-Code/blob/main/examples/altErrEst20.png?raw=true)
\
![test140ft](https://github.com/jludeman-1/Ludeman-Thesis-Code/blob/main/examples/altErrEst140.png?raw=true)
\
The primary code used for the prediction of runway altitude based on four points along the runway edge or two runway corners.
\
The code will be slowly added as it is cleaned up.\
The code used can be found in the thesis paper in the appendix. The code uploaded here will be a more unified program with a short explanation. All of this information can be found in the thesis, but this will be significantly more compact.
