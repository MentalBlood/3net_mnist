import mxnet.ndarray as nd
from dataPreprocessing import prepareData
from loadNets import nets

def processThroughNet(net, data, labels):
	data = nd.transpose(nd.array(data), (0, 3, 1, 2))
	out = net(data)
	predictions = nd.argmax(out, axis=1).asnumpy()
	return [(int(p), labels[int(p)]) for p in predictions]

def prepareAndProcessThroughNet(netName, data):
	net = nets[netName]['net']
	labels = nets[netName]['labels']
	preparedData = prepareData(data)
	return processThroughNet(net, preparedData, labels)