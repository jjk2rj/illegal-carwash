# Dependencies
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import os
# CNN Config
classifier = Sequential()
classifier.add(Conv2D(32, (64, 64), input_shape = (1024, 1024, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (8, 8)))
classifier.add(Conv2D(32, (64, 64), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (8, 8)))
classifier.add(Flatten())
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# Train CNN
os.chdir('/Users/romanwang/Work/Personal/projects/illegal-carwash/models')
train_datagen = ImageDataGenerator(rescale = 1./255, validation_split = 0.2)
train_generator = train_datagen.flow_from_directory('./img/resized',batch_size = 32,class_mode = 'binary', target_size=(1024, 1024), subset='training')
validation_generator = train_datagen.flow_from_directory('./img/resized',batch_size = 32,target_size=(1024, 1024),class_mode = 'binary', subset='validation')
classifier.fit_generator(train_generator, steps_per_epoch = 16, epochs = 25, validation_data = validation_generator, validation_steps = 16)
# Predict Image
test_image = image.load_img('./img/test/car_wash.jpg', target_size = (1024, 1024))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
prediction = 'car_wash'
else:
prediction = 'non_car_wash'
