# Image-Processing-Assignment
Distortion and zooming of images done using Python and OpenCV


**Program 1: Distorting image**

Given an image, the program distorts the image according to the given co-ordinates. The program accepts the image path, and the co-ordinates as arguments. Geometric transformation was done using OpenCV's inbuilt library, getPerspectiveTransform and warpPerspective.
On running the program, the image is distorted as per the given co-ordinates and saved as final.jpg

_To run:_

python distortimg.py <img_path_name> <x1_coord> <y1_coord> <x2_coord> <y2_coord> <x3_coord> <y3_coord> <x4_coord> <y4_coord>



**Program 2: Zooming image**

Zoooming an image, given the pivot co-ordinates and scale of zooming. No OpenCV library was used apart from loading and saving the image. According to the scale, an area of the image around the pivot co-ordinates, was captured (the area captured was proportional to the height and width of the original image, so as to maintain aspect ratio). Then interpolation had to be done to bring the image to the size of the original image. There are many methods of interpolation possible. In this program, Bilinear interpolation was used. The scale of zooming is an integer value, starting from value 1, where 1 is 1x and is the same image without zooming, 2 is 2x and is equivalent to 200% zooming, and so on..

_To run:_

python zooming.py <img_path_name> <x_coord> <y_coord> <scale_of_zooming>

**NOTE:** 

The format of the co-ordinates given for both the programs, should be as follows:-

- No commas between the x-coordinate and y-coordinate
- The x-coordinate corresponds to the **width** of the image, and hence the max value that x can take is (width-1)
- The y-coordinate corresponds to the **height** of the image, and hence the max value that y can take is (height-1)
- The co-ordinate pairs (A,B,C,D) given for the first program, should be such that A,B,C,D are in clockwise direction or anti-clockwise direction. The order shouldn't be messed up.

**NOTE 2:**

The second program takes time for execution, as it traverses through every pixel of the area of interest of the image. It could take around 10 seconds to 25 seconds for a medium sized image and with scale of zooming between 2 to 5
