import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.layers.normalization import BatchNormalization
# from keras.layers.convolutional import *
# from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools
# import matplotlib.pyplot as ply
# %matplotlib inline

file_classes = ['dogs', 'cats']

epochs = 20

train_path = 'data/train'
valid_path = 'data/valid'
test_path = 'data/test'

train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(224,224), classes=file_classes, batch_size=10)
valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(224, 224), classes=file_classes, batch_size=4)
# test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(224, 224), classes=file_classes, batch_size=8)

imgs, labels = next(train_batches)

vgg16_model = keras.applications.vgg16.VGG16()


#Convert to a Sequential Model Type
model = Sequential()
for layer in vgg16_model.layers[:-1]:
    model.add(layer)

for layer in model.layers:
    layer.trainable = False


model.add(Dense(len(file_classes), activation='softmax'))

model.summary()

model.compile(Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit_generator(train_batches, steps_per_epoch=4,
					validation_data=valid_batches, validation_steps=4, epochs=epochs, verbose=2)


json = model.to_json()
with open('models/model.json', 'w') as json_file:
	json_file.write(json)

model.save_weights('models/model_weights.h5')

model.save('models/model_complete.h5')
print("Saved Model")

# def preprocess_image(image, target_size):
# 	if image.mode != 'RGB':
# 		image = image.convert('RGB')

# 	image = image.resize(target_size)
# 	image = img_to_array(image)
# 	image = np.expand_dims(image, axis=0)

# 	return image

# img = preprocess_image(load_img('./test_img.jpg'), target_size=(224, 224))
# print("Making Test Prediction")
# predict = model.predict(img)

# print(predict)