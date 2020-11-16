from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)

import loadNets

from loadAPIs import loadAPIs
api = loadAPIs(app)

if __name__ == '__main__':
	app.run()