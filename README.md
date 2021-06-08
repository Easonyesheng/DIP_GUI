## Environment  

python 3.7.1
opencv-python 4.5.1  

You can use `image_gui.yaml` to build the same environment. 

## RUN

   > python main.py

You can change the values in the `settings.py` to change the window size and position to suit different PC's resolutions. 

## Main Operations

### Histogram & Thresholding  

This part contains some basic algorithms.  

  1. Input original image.  
  2. Get the Gary image.  
  3. Get the Histogram.  
  4. OTSU & Entropy Thresholding.  

### Convolution  

This part contains convolution operations using different filters to enhance or blur images. 

It includes three classes of convolution  

   1. Edge detection 
       using sobel, prewitt and Robert masks  
   2. blur
       using Gaussian and Median filter  
   3. DIY Convolution 
       using your own filter  

### Morphology  

It's about morphology operations. 
You can set your own SE size and check the running time. 
Note: because of pyqt's show problem, I use some save&read trick.  

  1. Basic operations including Dilation, Erosion, open and close.  
  2. Distance Translation & Conditional Dilation.  
  3. Skeleton get & Morphology Edge detection.  

### Gray Morphology  

Some Gray Morphology operations.  

  1. Gray Dilation, Erosion, Open, Close.  
  2. Gray Reconstruction. --OBR & CBR.  
  3. Gray Morphology Gradient.  

## Contributor

[LucyT](https://github.com/lucyttttt)
