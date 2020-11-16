from flask import Flask
app = Flask(__name__)

import loadNets

from loadAPIs import loadAPIs
metaAPI = loadAPIs(app)

if __name__ == '__main__':
	app.run()