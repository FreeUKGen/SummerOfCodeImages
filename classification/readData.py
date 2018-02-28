import numpy as np 
from PIL import Image
import os
from tqdm import tqdm
from scipy.misc import imresize
import csv

# Read label classification file, construct data
def getData(imageDirPrefix, filePath):
	X = []
	Y = []
	with open(filePath, 'r') as f:
		reader = csv.reader(f)
		for line in tqdm(reader):
			filePath = line[0]
			imgClass = line[1]
			# Read image as a black&white image
			image = np.asarray(Image.open(os.path.join(imageDirPrefix, filePath)).convert('L'))
			# Resize into a smaller image
			image = imresize(image, (150, 250))
			X.append(image)
			Y.append(imgClass)
	X = np.array(X)
	X = X.reshape(X.shape + (1,))
	# Also store the mapping between class-names and indices
	mappingDict = dict([(y,x) for x,y in enumerate(sorted(set(Y)))])
	Y = np.array([ mappingDict[x] for x in Y])
	return X, Y, mappingDict


if __name__ == "__main__":
	import sys
	X, Y, mapping = getData(sys.argv[1], sys.argv[2])
	print X.shape, Y.shape

