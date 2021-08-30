# imports
import census_dictionary
from flask import Flask, request, jsonify

# load data from census dictionary
states = census_dictionary.states

# extract state data
def extract(value, category):
	# find state
	state = {}
	for s in states:
		for key in s:
			if str(key) == str(value):
				state = s
				
	if len(state) == 0:
		return 'invalid state'

	if category == 'all':
		return jsonify(state[value])

	if category == 'overview':
		return jsonify(state[value]['overview'])

	if category == 'population':
		return jsonify(state[value]['population'])

	if category == 'income':
		return jsonify(state[value]['income'])

	if category == 'education':
		return jsonify(state[value]['education'])

	if category == 'employment':
		return jsonify(state[value]['employment'])

	if category == 'housing':
		return jsonify(state[value]['housing'])

	if category == 'health':
		return jsonify(state[value]['health'])

	if category == 'economy':
		return jsonify(state[value]['economy'])

	if category == 'family':
		return jsonify(state[value]['family'])

	if category == 'race':
		return jsonify(state[value]['race'])


# create the Flask app
app = Flask(__name__)

# return all the data for the state
@app.route('/')
def entire():
	name = request.args['state']
	if 'state' in request.args:
		return extract(name, 'all')
	return 'invalid input'		

# get an overview of data for the state
@app.route('/overview')
def overview():
	name = request.args['state']
	if 'state' in request.args:
		return extract(name, 'overview')
	return 'invalid input'

	
# get the population data for the state
@app.route('/population')
def population():
	name = request.args['state']
	if 'state' in request.args:
		return extract(name, 'population')
	return 'invalid input'


# get the income data for the state
@app.route('/income')
def income():
	name = request.args['state']
	if 'state' in request.args:
		return extract(name, 'income')
	return 'invalid input'


# get the education data for the state
@app.route('/education')
def education():
	name = request.args['state']
	if 'state' in request.args:
		return extract(name, 'education')
	return 'invalid input'


# get the employment data for the state
@app.route('/employment')
def employment():
	name = request.args['state']
	if 'state' in request.args:
		return extract(name, 'employment')
	return 'invalid input'


# get the housing data for the state
@app.route('/housing')
def housing():
	name = request.args['state']
	if 'state' in request.args:
		return extract(name, 'housing')
	return 'invalid input'


# get the health data for the state
@app.route('/health')
def health():
	name = request.args['state']
	if 'state' in request.args:
		return extract(name, 'health')
	return 'invalid input'


# get the economy data for the state
@app.route('/economy')
def economy():
	name = request.args['state']
	if 'state' in request.args:
		return extract(name, 'economy')
	return 'invalid input'


# get the family data for the state
@app.route('/family')
def family():
	name = request.args['state']
	if 'state' in request.args:
		return extract(name, 'family')
	return 'invalid input'


# get the race data for the state
@app.route('/race')
def race():
	name = request.args['state']
	if 'state' in request.args:
		return extract(name, 'race')
	return 'invalid input'		


if __name__ == '__main__':
	app.run(debug = True)



