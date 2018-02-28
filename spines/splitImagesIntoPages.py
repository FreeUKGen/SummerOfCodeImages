import numpy as np 
from PIL import Image
import os
import cv2
from tqdm import tqdm

# Detect Cany-edges using the given sigma, for the provided input image
def auto_canny(image, sigma=0.33):
	v = np.median(image)
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	return edged

# Extract central area fo the given image (as the centre of two pages is likely to be in this region)
def getRelevantArea(image, sideRatio=0.1):
	side = image.shape[1]
	leftSide = int((0.5 - sideRatio) * side)
	rightSide = int((0.5 + sideRatio) * side)
	return image[:, leftSide:rightSide], int((0.5 - sideRatio)*side)

# Calculate the optimal straight line that splits the image into 2 pages
def getOptimalStraightLine(image):
	scores = np.sum(image, axis=0)
	return np.argmin(scores)

# Split images in a given directory into 2 pages per image, and dump them in the output directory
def splitImagesIntoPages(directory, outputDirectory):
	for file in tqdm(os.listdir(directory)):
		imagePath = os.path.join(directory, file)
		# Extract filename for later use
		fileName = file.split('.')[0]
		# Open image in original mode
		rawImage = Image.open(imagePath)
		# Convert image to B/W
		readImage = np.asarray(rawImage.convert('L'))
		rawImage = np.asarray(rawImage)
		# Extract central area from B/W image
		trimmedImage, leftSide = getRelevantArea(readImage)
		# Get Canny-edge image for the above
		edgeImage = auto_canny(trimmedImage, 0.5)
		# Split given edge-image into 2 vertically
		splitLine = getOptimalStraightLine(edgeImage)
		# Split image into 2 pages using above calculations
		leftImage = rawImage[:, :splitLine + leftSide]
		rightImage = rawImage[:, splitLine + leftSide:]
		# Save these pages as two different images
		leftPage = Image.fromarray(leftImage)
		leftPage.save(os.path.join(outputDirectory, fileName + '_left.jpeg'))
		rightPage = Image.fromarray(rightImage)
		rightPage.save(os.path.join(outputDirectory, fileName + '_right.jpeg'))


if __name__ == "__main__":
	import sys
	splitImagesIntoPages(sys.argv[1], sys.argv[2])

