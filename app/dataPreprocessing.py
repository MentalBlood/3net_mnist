import cv2
import numpy as np
import base64

def prepareImage(imageString):
	imageBytes = base64.decodebytes(imageString.encode('utf-8'))
	nparr = np.frombuffer(imageBytes, np.uint8)
	grayscale = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
	return np.array(grayscale.astype(np.float32)/255).reshape(28, 28, 1)

def prepareData(data):
	return list(map(prepareImage, data))