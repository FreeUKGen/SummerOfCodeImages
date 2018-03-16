# Census Image Classfication

### Methodology

* Preprocess image : crop edges to alter frame to form
* Resize image to (430, 250)
* Training on a Convolutional Neural Netowrk model with a learning rate of 1e-6 owing to low dataset
* Obtained accuracy = 95.6%

### Image preprocessing

Raw dataset image before preprocessing:

![dataset image](https://github.com/salonirk11/census_image_classfication/blob/master/img_raw.jpg)


The raw image was thresholded to ```binary``` colours. Thereafter, using a combination of ```findContours``` and ```boundingRect``` methods of ```OpenCV```, the form was brought into focus remvoing all the extra portions of the image.
Following this, image was resized to (430, 250) to retain sufficient features and to maintain the proportion of the form.

The image obtained afer preprocessing on the above image :

![processed image](https://github.com/salonirk11/census_image_classfication/blob/master/img_proc.jpg)


### Training

The processed dataset was trained on a convolutional neural model. ```BatchNormalisation```, ```MaxPooling``` were used in this model with ```relu``` as activation.


To run the model use the following command:
```
python train.py <path of directory with images> <path of csv file>
```

For example:
```
python train.py images/freecen data/gold/combined_classifications_20180227.csv
```

### Optimization

Following is the learning curve for a learing rate of 1e-6

![learning_rate](https://github.com/salonirk11/census_image_classfication/blob/master/Figure_1.png)
