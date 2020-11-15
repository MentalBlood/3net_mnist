from flask import Flask, request
from flask_restful import Api

from loadNets import loadNets

nets = loadNets()
print(nets)

app = Flask(__name__)
api = Api(app)

from dataPreprocessing import prepareData, prepareImage
from processThroughNet import processThroughNet

@app.route('/classify', methods=['POST'])
def classify():
	netName = request.get_json()['dataset']
	net = nets[netName]['net']
	data = request.get_json()['images']
	labels = nets[netName]['labels']
	preparedData = prepareData(data)
	return processThroughNet(net, preparedData, labels)

if __name__ == '__main__':
	app.run()