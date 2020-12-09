#to change the file/string by using json to python.
import json
# from HTTPBA import *

#<filename>->jsonfile transfer python


def readConfig(file:str) :
	try:
		js = json.load(file)
		return js
	except ValueError as e:
		print("invalid json: %s" % e)
		return None
	except AttributeError as e:
		print("Attribute Error: %s" %e)
		return None

#save the data
def writeConfig(filename:str,data:list) :
	string = ""
	for x in data:
		string += (x+"\n")
	with open(file=filename, mode='w') as f:
		f.write(string)