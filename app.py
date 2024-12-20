import json

with open('temp.json','r',encoding = 'UTF-8') as f:
	data = json.load(f)
	print(data)