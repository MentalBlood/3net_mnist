from ..common import *

@routedTo(['/classify'], 'classify')
class Classify(Resource):
	def post(self):
		request_json = request.get_json()
		if request_json['dataset'] != None:
			available_nets = ['MNIST', 'FashionMNIST', 'distributor']
			net_name = request.get_json()['dataset']
			if not (net_name in available_nets):
				return {'error': 'no net with such name'}
			data = request.get_json()['images']
			predictions = prepareAndProcessThroughNet(net_name, data)
			predictions = [{
				'class': p[0],
				'label': p[1]
			} for p in predictions]
			return {'predictions': predictions}
		else:
			data = request.get_json()['images']
			preparedData = prepareData(data)
			suitable_nets = processThroughNet(nets['distributor']['net'], preparedData, nets['distributor']['labels'])
			images_indexes_by_suitable_nets_names = {}
			net_name_by_answer_label = {
				'MNIST': 'MNIST',
				'Fashion MNIST': 'FashionMNIST'
			}
			for d in range(len(suitable_nets)):
				answer_label = suitable_nets[d][1]
				net_name = net_name_by_answer_label[answer_label]
				if not (net_name in images_indexes_by_suitable_nets_names):
					images_indexes_by_suitable_nets_names[net_name] = {}
					images_indexes_by_suitable_nets_names[net_name]['distributor_answer'] = answer_label
					images_indexes_by_suitable_nets_names[net_name]['images_indexes'] = []
				images_indexes_by_suitable_nets_names[net_name]['images_indexes'].append(d)
			
			answersDict = {}
			for suitable_net_name in images_indexes_by_suitable_nets_names:
				images_indexes = images_indexes_by_suitable_nets_names[suitable_net_name]['images_indexes']
				dataset = images_indexes_by_suitable_nets_names[suitable_net_name]['distributor_answer']
				images = [preparedData[i] for i in images_indexes]
				suitable_net = nets[suitable_net_name]['net']
				labels = nets[suitable_net_name]['labels']
				answers = processThroughNet(suitable_net, images, labels)
				for i in range(len(answers)):
					answer = answers[i]
					answer = {
						'dataset': dataset,
						'class': answer[0],
						'label': answer[1]
					}
					answersDict[images_indexes[i]] = answer

			answersList = [answersDict[i] for i in sorted(answersDict.keys())]
			
			return answersList