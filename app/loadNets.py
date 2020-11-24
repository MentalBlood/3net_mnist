import os
import json
from mxnet.gluon import nn

def loadNets(path = './net/'):
	print('loadNets')
	nets = {}

	models_dirs = os.listdir(path)

	for model_dir in models_dirs:
		model_dir_path = path + model_dir + '/'
		if os.path.isdir(model_dir_path):
			arch_file_path = model_dir_path + 'symbol.json'
			params_file_path = model_dir_path + 'params.params'
			labels_file_path = model_dir_path + 'labels.json'
			model_name = model_dir
			with open(labels_file_path) as labels_file:
				nets[model_name] = {
					'net': nn.SymbolBlock.imports(arch_file_path, ['data'], params_file_path),
					'labels': json.load(labels_file)
				}

	return nets

nets = loadNets()