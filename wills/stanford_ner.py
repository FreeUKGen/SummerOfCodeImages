from PIL import Image
import pytesseract
import argparse
import cv2
import os
import csv
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

ocr = []

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
args = vars(ap.parse_args())

reader = csv.reader(open('data/gold/extracted_wills.csv'))
for row in reader:
    filename = args["image"].split('/')[-1].split('.')[0]
    if(row[0] == filename):

        # extract the (x,y) rectangular coordinates for each entry in the probate book
        x1 = int(row[2])
        y1 = int(row[3])
        x2 = int(row[4])
        y2 = int(row[5])

        # load the example image and convert it to grayscale and crop
        image = cv2.imread(args["image"])
        image = image[y1:y2, x1:x2]
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
        filename1 = "{}.png".format(os.getpid())
        cv2.imwrite(filename1, gray)

        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        text = pytesseract.image_to_string(Image.open(filename1))
        print(text)
        os.remove(filename1)

        # apply stanford entity recognizer to the data extracted by ocr

        st = StanfordNERTagger('/usr/bin/stanford-ner-2018-02-27/classifiers/english.muc.7class.distsim.crf.ser.gz', '/usr/bin/stanford-ner-2018-02-27/stanford-ner.jar', encoding='utf-8')

        tokenized_text = word_tokenize(text)
        classified_text = st.tag(tokenized_text)

        print(classified_text)
