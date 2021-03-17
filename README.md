# DIP_GUI

My first repository.  
It's a GUI based on PYQT5 and python-opencv to perform **Digital Image Process**(DIP) which contains 4 projects.  

## Environment  

   macOS Mojave 10.14.6  
   python 3.7.1  
   opencv-python 4.1.2  

## RUN

   > python /.../ImageInput.py  
  Before running, must set the right path parameters.  
  
## Main Operations

### Histgram & Thresholding  

This part contains some basic algorithms.  

  1. Input original image.  
  2. Get the Gary image.  
  3. Get the Hisgram.  
  4. OTSU & Entropy Thresholding.  

### Convolution  

This part contains convlution operations using different filters to enhance or blur images.  
It includes three classes of convlution  

   1. Edge detection  
       using sobel, prewitt and Robert masks  
   2. blur  
       using Guassian and Median filter  
   3. DIY Convlution  
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
  3. Gray Moorphology Gradient.  
