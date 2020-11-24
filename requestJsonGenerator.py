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
					choices=['MNIST', 'FashionMNIST'],
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
		imageBytes = image.read()
		result = base64.encodebytes(imageBytes).decode("utf-8")
	return result
img = list(map(readImage, imgPaths))
jsonString = None
if netName:
	jsonString = json.dumps({'images': img, 'dataset': netName})
else:
	jsonString = json.dumps({'images': img})
print(jsonString)