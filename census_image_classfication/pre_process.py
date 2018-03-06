import cv2
from matplotlib import pyplot as plt
import csv
import os
import numpy as np
from tqdm import tqdm

def proc(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,img = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
    (_,cnts, _) = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x_, y_, w_, h_ = 0, 0, 0, 0
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w>500 and h>500 and w*h > w_*h_:
            w_=w
            h_=h
            x_=x
            y_=y
    new_img = img[y_:y_+h_,x_:x_+w_]
    new_img = cv2.cvtColor(new_img, cv2.COLOR_GRAY2BGR)
    img = cv2.resize(new_img,(430,250))
    cv2.imwrite("img.jpg", new_img)
    img=np.array(img)
    return img


def read_im(path):
    img = cv2.imread(path)
    img = proc(img)
    return img

def train_data(im_dir, src_file):
    img_list= []
    labels_list= []
    with open('file.csv', 'r') as f:
        reader = csv.reader(f)
        for line in tqdm(reader):
            img_list.append(read_im(os.path.join(im_dir,line[0])))
            labels_list.append(line[1])
        img_list=np.array(img_list)
    return img_list, labels_list
