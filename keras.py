
import numpy as np
from random import randint
from sklearn.preprocessing import MinMaxScaler

train_labels = []
train_samples = []

for i in range(1000):
	random_younger = randint(13, 64)
	train_samples.append(random_younger)
	train_labels.append(0)

	random_older = randint(65, 100)
	train_samples.append(random_older)
	train_labels.append(1)

for i in range(50):
	random_younger = randint(13, 64)
	train_samples.append(random_younger)
	train_labels.append(0)

	random_older = randint(65, 100)
	train_samples.append(random_older)
	train_labels.append(1)


for i in train_samples:
	print(i)

train_labels = np.array(train_labels)
train_samples = np.array(train_samples)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_samples = scaler.fit_transform((train_samples).reshape(-1, 1))

for i in scaled_train_samples:
	print(i)

#----------------------------------------------

import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy

model = Sequential([
	Dense(16, input_shape=(1,), activation='relu'),
	Dense(32, activation='relu'),
	Dense(2, activation='softmax')
])

# model.add()

model.summary()

model.compile(Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(scaled_train_samples, train_labels, batch_size=10, epochs=20, shuffle=True, verbose=2)