import json

with open('test.json') as json_file:
	data = json.load(json_file)
	if data:
		print(data)