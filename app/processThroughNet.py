import mxnet.ndarray as nd

def processThroughNet(net, data, labels):
	data = nd.transpose(nd.array(data), (0, 3, 1, 2))
	out = net(data)
	predictions = nd.argmax(out, axis=1).asnumpy()
	print(out)

	if labels:
		return {'predictions': [(int(p), labels[int(p)]) for p in predictions]}
	else:
		return {'predictions': [int(p) for p in predictions]}