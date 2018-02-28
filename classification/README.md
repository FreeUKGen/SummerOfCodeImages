## Classification of images into entry/other

### Proposed Technique
* Convert all images into Black&White.
* Downsize all images into (150, 250)
* Define a simple CNN-classifier and train it on the given data
* Batch-normalization is used to handle the variance in given data, while automatic class-weights are used to balance the error function (as the class distribution is biased)
* To account for the low amount of data given, a small learning rate is used (to avoid overfitting)

### Running it
* Run `python trainClassifier.py <images_folder> <label_file>` from the current directory to train an end-to-end model.
* For example, run `python trainClassifier.py images/freecen/ data/gold/combined_classifications_20180227.csv`
