import csv
import flask
from flask import request

app = flask.Flask(__name__)

results = []

def read_cvs():
	with open('test.csv') as file:
		keys = ['name', 'Occupation', 'Income']
		reader = csv.DictReader(file, fieldnames=keys)
		for row in reader:
			results.append(dict(row))


def tester(name):
	for res in results:
		for key in res:
			if key == 'name' and res[key] == name:
				return res
	return 'Not Valid'


@app.route('/', methods=['GET'])
def home():
	name = str(requests.arg['name'])
	return tester(name)
