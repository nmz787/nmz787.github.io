# Using Python and openCV to extract and manipulate plot lines

Someone on the PLOTS-spectrometry mailing list posted a spectrograph they'd collected with their PLOTS-spectrometer, and also a plot the LED manufacturer provided.  
The wondered why their spectrogram didn't look like either of the two plots provided by the manufacturer, and I thought they might look similar if the plot lines were added or multiplied with each other.  
So I made this script to select the plot line color, then extract colors close to that into separate images.  
With these images, the maximum Y value for each column was found, and Y values from the corresponding plots were added and also multiplied, then saved to new output images.

## LED spectrogram
![Input dual-line plot](../img/Cree_A19_warm_2700k.JPG)  
&nbsp;  
&nbsp;  

## Using this dual-line graph as input

![openCV image](../img/opencv_combine_plot/two_line_plot_cropped.png )  
&nbsp;  

## These binary images were extracted of the individual plot lines

![openCV image](../img/opencv_combine_plot/two_line_out/two_line_plot_cropped_extracted_0.png )  

![openCV image](../img/opencv_combine_plot/two_line_out/two_line_plot_cropped_extracted_1.png )  

## Plots' Y-values added together

![openCV image](../img/opencv_combine_plot/two_line_out/two_line_plot_cropped_added.png )  

## Added, then divided by 2  

![openCV image](../img/opencv_combine_plot/two_line_out/two_line_plot_cropped_added_scaled.png )  

## Square root of the multiples ( sqrt(y1 * y2) )  

![openCV image](../img/opencv_combine_plot/two_line_out/two_line_plot_cropped_multiplied.png )  

## Graph of added (yellow) and multiplied (red) lines, both were scaled down.

![openCV image](../img/opencv_combine_plot/two_line_out/two_line_plot_cropped_multiplied_plus_added.png "blog_thumbnail")  

&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  


## Using this triple-line graph image as input  

![openCV image](../img/opencv_combine_plot/triple_line_plot_cropped.png )  

## The results from processing:  
## Binary images of extracted plots

![openCV image](../img/opencv_combine_plot/triple_line_out/triple_line_plot_cropped_extracted_0.png )  

![openCV image](../img/opencv_combine_plot/triple_line_out/triple_line_plot_cropped_extracted_1.png )  

![openCV image](../img/opencv_combine_plot/triple_line_out/triple_line_plot_cropped_extracted_2.png )  

## Added

![openCV image](../img/opencv_combine_plot/triple_line_out/triple_line_plot_cropped_added.png )  

## Added then divided by 3

![openCV image](../img/opencv_combine_plot/triple_line_out/triple_line_plot_cropped_added_scaled.png )  

## Cube root of the multiples ( cube_root(y1 * y2 * y3) )

![openCV image](../img/opencv_combine_plot/triple_line_out/triple_line_plot_cropped_multiplied.png )  

## Graph of added (yellow) and multiplied (red) lines, both were scaled down.

![openCV image](../img/opencv_combine_plot/triple_line_out/triple_line_plot_cropped_multiplied_plus_added.png )  





&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
## Check out the code I wrote to do this [here](https://github.com/nmz787/opencv-snippets/blob/master/python/combine_plot.py)
