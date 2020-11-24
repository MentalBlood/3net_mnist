import requests
import json
import base64
import argparse

defaultImagesPaths = [
	'fashion-mnist_png\\test\\1\\2.png',
	'mnist_png\\testing\\2\\1.png',
	'mnist_png\\testing\\4\\4.png',
	'fashion-mnist_png\\test\\5\\8.png'
]

parser = argparse.ArgumentParser(description='Generate JSON for request')
parser.add_argument('--dataset', type=str, nargs='?',
					choices=['MNIST', 'FashionMNIST', 'distributor'],
                    help='dataset model should be trained on')
parser.add_argument('--images', metavar='image', type=str, nargs='+',
                    help='paths to files to send in request',
                    default=defaultImagesPaths)
args = parser.parse_args()

imgPaths = args.images
netName = args.dataset
def readImage(path):
	result = None
	with open(path, 'rb') as image:
		imageBytes = open(path, 'rb').read()
		result = base64.encodebytes(imageBytes).decode("utf-8")
	return result
img = list(map(readImage, imgPaths))
if netName:
	requestJson = {'images': img, 'dataset': netName}
else:
	requestJson = {'images': img}
print('request json:', json.dumps(requestJson))

testUrl = 'http://localhost:8080/v2/classify'
headers = {'content-type': 'application/json'}
response = requests.post(testUrl, json=requestJson, headers=headers)
print('response json:', response.text)