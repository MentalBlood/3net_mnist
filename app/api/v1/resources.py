from ..common import *

@routedTo(['/classify'], 'classify')
class Classify(Resource):
	def post(self):
		availableNets = ['MNIST', 'FashionMNIST']
		netName = request.get_json()['dataset']
		if not (netName in availableNets):
			return {'error': 'no net with such name'}
		net = nets[netName]['net']
		data = request.get_json()['images']
		labels = nets[netName]['labels']
		preparedData = prepareData(data)
		predictions = processThroughNet(net, preparedData, labels)
		predictions = [{
			'class': p[0],
			'label': p[1]
		} for p in predictions]
		return {'predictions': predictions}