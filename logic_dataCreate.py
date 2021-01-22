import numpy as np
import pandas as pd
import os
import cv2
import glob
import matplotlib.pyplot as plt
import time



x = 802
y = 800
xp = x + 16
yp = y + 16

path = r"C:\Users\user\Desktop\vsyakoe\lesPyrhon\dataScince\neiro_foto\app_dataCreate"
name = "/branch"
expansion = ".jpg"
image = cv2.imread(path+name+expansion)
imageArray = None
ansArray = None


def Part_image(right = 0, up = 0, path = path, name = name, expansion = expansion, image = image):
	global x
	global y
	global xp
	global yp

	image8x8 = image.copy()
	imageRec = image.copy()
	yr, xr, ch = image.shape
	try:
		pix = 16
		pix2 = 100
		x += right*pix
		xp += right*pix
		y += up*pix
		yp += up*pix

		image8x8 = image8x8[y:yp,x:xp]
		cv2.rectangle(imageRec, (x, y) , (xp, yp), (0, 255, 255), 1)
		cv2.rectangle(image, (0+100, yr-20) , (xr-20, 100), (0, 0, 255), 1)
		imageRec = imageRec[y-pix2:yp+pix2,x-pix2:xp+pix2]
		imageRec = cv2.cvtColor(imageRec, cv2.COLOR_BGR2RGB)
	except:
		pass
	else:
		pass
	finally:
		image8x8 = cv2.cvtColor(image8x8, cv2.COLOR_BGR2RGB)
	return image8x8, imageRec

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def SaveAnsArray(ans):
	global imageArray
	global ansArray
	image8x8, imgGarb = Part_image()

	if imageArray is None:
		imageArray = image8x8.reshape(1, *image8x8.shape)
	else:
		imageArray = np.row_stack([imageArray, image8x8.reshape(1, *image8x8.shape)])


	if ansArray is None:
		ansArray = np.array(ans)
	else:
		ansArray = np.row_stack([ansArray, ans])

	# print(ansArray)
	# ansArray = np.()




	np.savez('dataset_image_neiro', imageArray = imageArray, ansArray = ansArray)



def SaveDataset():
	np.savez('dataset_image_neiro', imageArray = imageArray, ansArray = ansArray)
	print("save complete")

def LoadDataset():
	if os.path.isfile("dataset_image_neiro.npz"):
		data = np.load("dataset_image_neiro.npz", allow_pickle = True)
		print("load complete")
		print(data["ansArray"])

		return data["imageArray"], data["ansArray"] 


