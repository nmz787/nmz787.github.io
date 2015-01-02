# Using Python and openCV to extract and manipulate plot lines

Someone on the PLOTS-spectrometry mailing list posted a spectrograph they'd collected with their PLOTS-spectrometer, and also a plot the LED manufacturer provided.  
The wondered why their spectrogram didn't look like either of the two plots provided by the manufacturer, and I thought they might look similar if the plot lines were added or multiplied with each other.  
So I made this script to select the plot line color, then extract colors close to that into separate images.  
With these images, the maximum Y value for each column was found, and Y values from the corresponding plots were added and also multiplied, then saved to new output images.

## LED spectrogram
![Input dual-line plot](../img/Cree_A19_warm_2700k.JPG)  
&nbsp;  
&nbsp;  

## Input dual-line graph
![LED spectrogram](../img/xbd.png)  
&nbsp;  

## Graph of added (yellow) and multiplied (red) lines, both were scaled down.
![Combined plot](../img/xbd_combined.png "blog_thumbnail")  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
## Check out the code I wrote to do this [here](https://github.com/nmz787/opencv-snippets/blob/master/python/combine_plot.py)
