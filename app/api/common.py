def routedTo(urls, endpoint):
	def initFunc(self):
		self.urls = urls
		self.endpoint = endpoint
	def decorator(someClass):
		someClass.__init__ = initFunc
		return someClass
	return decorator