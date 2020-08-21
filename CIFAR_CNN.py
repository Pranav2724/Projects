import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import cifar10
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, Dropout,BatchNormalization,MaxPooling2D
from keras.regularizers import *

cifar10.data_path = "C:\\Users\\prankhur\\OneDrive - Qualcomm\\Desktop\Python codes\\Cifar10"
cifar10.maybe_download_and_extract()
class_names = cifar10.load_class_names()
images_train, cls_train, labels_train = cifar10.load_training_data()
images_test, cls_test, labels_test = cifar10.load_test_data()


model = Sequential()
#add model layers
model.add(Conv2D(filters=32, kernel_size=3, activation='relu', strides=1,kernel_regularizer=l2(1e-4),padding='SAME', input_shape=(32,32,3)))
model.add(BatchNormalization())
model.add(Conv2D(filters=32, kernel_size=3, strides=1, padding='SAME',kernel_regularizer=l2(1e-4), activation='relu'))
model.add(BatchNormalization())  # Used to improve speed, It normalizes the input layer by recentering
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(Conv2D(filters=64, kernel_size=3, strides=1, padding='SAME',kernel_regularizer=l2(1e-4), activation='relu'))
model.add(BatchNormalization())
model.add(Conv2D(filters=64, kernel_size=3, strides=1, padding='SAME',kernel_regularizer=l2(1e-4), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(Conv2D(filters=128, kernel_size=2, strides=1, padding='SAME',  kernel_regularizer=l2(1e-4), activation='relu'))
model.add(BatchNormalization())
model.add(Conv2D(filters=128, kernel_size=2, strides=1, padding='SAME',  kernel_regularizer=l2(1e-4), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.4))
model.add(Flatten())
model.add(Dense(units=10, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(images_train,labels_train,epochs=10)

pred = model.predict(images_test)
predictions = np.argmax(pred,1)
correct_predictions = tf.equal(predictions,cls_test) 

sess = tf.Session()
correct_pred = sess.run(correct_predictions)

pred_f = [class_names[i] for i in predictions]
pred_f = pd.DataFrame(pred_f)
pred_f.to_csv('results_CIFAR5.csv',index_label=False,index=False,header=False)