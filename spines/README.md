## Splitting images into 2 pages using Canny edge detector and pseudo-image-metadata

### How it Works

* A non machine-learning approach that does not require ground truth
* First, it converts the given image into black and white
* Then, it considers only 10% of the image, around the centre (on both sides, thus 20% of the image)
* On this copped image, Canny-edge detector is run
* Then, the sum of pixels for all possible vertical lines in this range is tried, and the one corresponding to the most black region (which is present in between any two pages) is used.
* Emperical analysis shows that this technique performs quite well for the given images


### Running it

* Simply run `python splitImagesIntoPages.py <images_Dir> <output_Images_Dir>`. For each image in the input directory, two images (with suffix '_left' and '_right') will be dumped into the output directory.
* For example, create a directory here named 'OutputImages', and then run `python splitImagesIntoPages.py images/freecen/1841/ OutputImages/`


