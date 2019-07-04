import numpy as np
import keras
from keras.utils import np_utils
from keras.models import load_model
# import matplotlib.pyplot as plt
import cv2


model = load_model('gen.h5')
while True:
	number = (input("Enter a number to generate (0-9) [q to exit]"))
	if number=="q":
		break
	number = int(number)
	cat_number = np_utils.to_categorical(number,10)
	cat_number = cat_number.reshape(1,10)
	img = model.predict(cat_number)
	img = img.reshape(28,28)
	cv2.imshow("Number {}".format(number),img)
	k = cv2.waitKey(0)
	cv2.destroyAllWindows()
	if k == 27:
		cv2.destroyAllWindows()
		break
	