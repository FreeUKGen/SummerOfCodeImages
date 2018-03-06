import pre_process
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

import keras
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam

def plot_rate(history):
    plt.subplot(211)
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')

    plt.subplot(212)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')

    plt.show()


def getSimpleCNN(input_shape, num_classes):
    inputs = Input(shape=input_shape)
    x = Conv2D(64, (3, 3), activation='relu')(inputs)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2, 2)) (x)
    x = Conv2D(32, (3, 3), activation='relu')(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2, 2)) (x)
    x = Conv2D(16, (3, 3), activation='relu')(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2, 2)) (x)
    x = Dropout(0.25)(x)
    x = Flatten()(x)
    x = Dense(64)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)
    out = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs, out)
    model.compile(loss=categorical_crossentropy,
                  optimizer=Adam(lr=1e-4),
                  metrics=['accuracy'])
    return model


if __name__=="__main__":
    x_train, y_train = pre_process.train_data(sys.argv[1], sys.argv[2])
    labels_set = list(set(y_train))
    labels_dict = {labels_set[i]:i for i in range(len(labels_set))}

    x_train = x_train.reshape(x_train.shape[0], 430, 250, 3)
    input_shape = (430,250,3)
    num_classes = len(labels_dict.keys())

    model = getSimpleCNN(input_shape, num_classes)
    y_train = np.array([labels_dict[x] for x in y_train])
    y_train = keras.utils.to_categorical(y_train, num_classes)

    batch_size = 4
    epochs = 18
    history = model.fit(
                x_train, y_train,
                batch_size=batch_size,
                epochs=epochs,
                validation_split=0.2
            )
    plot_rate(history)
