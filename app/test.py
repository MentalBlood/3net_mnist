# def makeClass(param):
# 	class A():
# 		def act(self):
# 			print('A acting!', param, 'self =', self)
# 	return A

# a = makeClass('chudesa')
# a_obj = a()
# a_obj.act()

# def getClasses():

# 	class A():
# 		def act(self):
# 			print('A acting!', 'self =', self)

# 	class B():
# 		def act(self):
# 			print('B acting!', 'self =', self)

# 	return [A, B]

# print(getClasses())


# import inspect

# def getClasses(moduleName):
# 	module = __import__(moduleName)
# 	print(dir(module))
# 	print(inspect.getmembers(module, inspect.isclass))
# 	classes = [m[1] for m in inspect.getmembers(module, inspect.isclass) if m[1].__module__ == moduleName]
# 	print(moduleName, 'classes:', classes)

# getClasses('test1')
# getClasses('api.v1.__init__')

import inspect
module = __import__('api.v1.test')
print(dir(module))
print(inspect.getmembers(module, inspect.isclass))
print(dir(getattr(module, 'v1')))
print(inspect.getmembers(module.v1, inspect.isclass))
print(dir(module.v1.test))
print(inspect.getmembers(module.v1.test, inspect.isclass))


# def routedTo(urls, endpoint):
# 	def initFunc(self):
# 		self.urls = urls
# 		self.endpoint = endpoint
# 	def decorator(someClass):
# 		someClass.__init__ = initFunc
# 		return someClass
# 	return decorator

# @routedTo(['/a'], 'a')
# class A():
# 	def post(self):
# 		return {'result': 'ok'}

# a = A()
# print(a.urls, a.endpoint)


# def f(a, *b, c):
# 	print('a =', a)
# 	print('b =', b)
# 	print('c =', c)

# a_should_be = 1
# b_should_be = (2, 3)
# c_should_be = 4

# f(a_should_be, *b_should_be, c=c_should_be)


# import test1
# import test2