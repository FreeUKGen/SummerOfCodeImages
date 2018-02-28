import readData
import model
import keras


if __name__ == "__main__":
	import sys
	# Load data
	X, Y, mapping = readData.getData(sys.argv[1], sys.argv[2])
	num_classes = len(mapping.keys())
	input_shape = X.shape[1:]
	# Loada simple CNN for tha classification task
	model = model.getSimpleCNN(input_shape, num_classes)
	Y = keras.utils.to_categorical(Y, num_classes)
	batch_size = 8
	epochs = 20
	# Train our model on the available data
	model.fit(X, Y, batch_size=batch_size, epochs=epochs, validation_split=0.2, class_weight='auto')

