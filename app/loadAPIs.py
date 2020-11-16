import os
import inspect

from flask_restful import Api

def getClasses(pathAsList):
	pathString = '.'.join(pathAsList)
	module = __import__(pathString)
	moduleItself = module
	for submodule in pathAsList[1:]:
		moduleItself = getattr(moduleItself, submodule)
	return [m[1] for m in inspect.getmembers(moduleItself, inspect.isclass) if m[1].__module__ == pathString]

def loadAPIs(app):
	APIs = {}

	apis_dirs = os.listdir('./api/')

	for api_dir in apis_dirs:
		if api_dir[0] != 'v':
			continue
		api_dir_path = './api/' + api_dir + '/'
		if os.path.isdir(api_dir_path):
			api_prefix = '/' + api_dir
			api = Api(app, prefix=api_prefix)
			resources = getClasses(['api', api_dir, 'resources'])
			for r in resources:
				api.add_resource(r, *r.urls, endpoint = api_prefix + '/' + r.endpoint)
			APIs[api_dir] = api

	return APIs