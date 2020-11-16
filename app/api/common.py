from flask import request
from flask_restful import Resource
from loadNets import nets
from dataPreprocessing import prepareData, prepareImage
from processThroughNet import *

def routedTo(urls, endpoint):
	def decorator(someClass):
		someClass.urls = urls
		someClass.endpoint = endpoint
		return someClass
	return decorator