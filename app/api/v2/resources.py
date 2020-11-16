from ..common import routedTo
from flask import request
from flask_restful import Resource
from loadNets import nets
from dataPreprocessing import prepareData, prepareImage
from processThroughNet import processThroughNet

@routedTo(['/classify'], 'classify')
class Classify(Resource):
	def post(self):
		availableNets = ['MNIST', 'FashionMNIST', 'distributor']
		netName = request.get_json()['dataset']
		if not (netName in availableNets):
			return {'error': 'no net with such name'}
		net = nets[netName]['net']
		data = request.get_json()['images']
		labels = nets[netName]['labels']
		preparedData = prepareData(data)
		return processThroughNet(net, preparedData, labels)