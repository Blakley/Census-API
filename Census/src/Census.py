import xpaths
import states

import csv
import pprint
from time import sleep
from selenium import webdriver

class Census():
	def __init__(self):
		self.states = states.data
		self.pp = pprint.PrettyPrinter(indent = 4)
		self.browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
		
		# data collection
		self.overview_data = [] 
		self.population_data = []
		self.income_data = []
		self.education_data = []
		self.employment_data = []
		self.housing_data = []
		self.health_data = []
		self.economy_data = []
		self.family_data = []
		self.race_data = []
		self.data_collection = [] # collection of all the data
		self.state_data = [] # all data from state
		self.navigate()

	def print_data(self):
		self.pp.pprint(self.state_data)

	def reset_data(self):
		self.overview_data = [] 
		self.population_data = []
		self.income_data = []
		self.education_data = []
		self.employment_data = []
		self.housing_data = []
		self.health_data = []
		self.economy_data = []
		self.family_data = []
		self.race_data = []
		self.data_collection = []

	# ------------------------------------
	#	visits the url for each state
	# ------------------------------------
	def navigate(self):
		sleep(3)

		i = 0
		for key in self.states:
			self.browser.get(self.states[key])
			sleep(10)

			# get the data from each section
			self.overview()
			self.populations_and_people()
			self.income_and_poverty()
			self.education()
			self.employment()
			self.housing()
			self.health()
			self.economy()
			self.family()
			self.race()
		
			# populate the current state array with the extracted data
			self.data_collection.append(self.overview_data)
			self.data_collection.append(self.population_data)	
			self.data_collection.append(self.income_data)
			self.data_collection.append(self.education_data)
			self.data_collection.append(self.employment_data)
			self.data_collection.append(self.housing_data)
			self.data_collection.append(self.health_data)
			self.data_collection.append(self.economy_data)
			self.data_collection.append(self.family_data)
			self.data_collection.append(self.race_data)
			self.state_data.append(self.data_collection)
			self.reset_data()

			sleep(2)

			i = i + 1
			if i == 10:
				break
			
		


	# ------------------------------------
	#	extracts the xpath data
	# ------------------------------------
	def helper(self, value, category):
		if category == 'overview':
			return self.browser.find_elements_by_xpath(xpaths.data[value])[0].text

		if category == 'population':
			return self.browser.find_elements_by_xpath(xpaths.population[value])[0].text

		if category == 'income':
			return self.browser.find_elements_by_xpath(xpaths.income[value])[0].text			

		if category == 'education':
			return self.browser.find_elements_by_xpath(xpaths.education[value])[0].text

		if category == 'employment':
			return self.browser.find_elements_by_xpath(xpaths.employment[value])[0].text

		if category == 'housing':
			return self.browser.find_elements_by_xpath(xpaths.housing[value])[0].text

		if category == 'health':
			return self.browser.find_elements_by_xpath(xpaths.health[value])[0].text

		if category == 'economy':
			return self.browser.find_elements_by_xpath(xpaths.economy[value])[0].text

		if category == 'family':
			return self.browser.find_elements_by_xpath(xpaths.family[value])[0].text

		if category == 'race':
			return self.browser.find_elements_by_xpath(xpaths.race[value])[0].text		
	

	# ------------------------------------
	#	returns an overview for the location
	# ------------------------------------
	def overview(self):
		data_overview = {
			'total_population' : '',
			'employment_rate' : '',
			'total_households' : '',
			'total_housing_units' : '',
			'median_household_income' : '',
			'bachelor_degree_or_higher' : '',
			'without_health_care_coverage' : '',
			'total_employer_establishments' : ''
		}

		data_overview['employment_rate'] = self.helper('employment_rate', 'overview')
		data_overview['total_population'] = self.helper('total_population', 'overview')
		data_overview['total_households'] = self.helper('total_households', 'overview')
		data_overview['total_housing_units'] = self.helper('total_housing_units', 'overview')
		data_overview['median_household_income'] = self.helper('median_household_income', 'overview')
		data_overview['bachelor_degree_or_higher'] = self.helper('bachelor_degree_or_higher', 'overview')
		data_overview['without_health_care_coverage'] = self.helper('without_health_care_coverage', 'overview')
		data_overview['total_employer_establishments'] = self.helper('total_employer_establishments', 'overview')
		self.overview_data.append(data_overview)
		

	# ------------------------------------
	#	gets various based on opulation
	# ------------------------------------
	def populations_and_people(self):
		data_overview = {
			'Median Age' : '',
			'Without an Internet Subscription': '',
			'Language Other Than English Spoken at Home' : '',
			'Foreign Born population' : '',
			'Moved From a Different State in the Last Year' : '',
			'Veterans in State' : ''
		}

		data_overview['Median Age'] = self.helper('Median Age', 'population')
		data_overview['Without an Internet Subscription'] = self.helper('Without an Internet Subscription', 'population')
		data_overview['Language Other Than English Spoken at Home'] = self.helper('Language Other Than English Spoken at Home', 'population')
		data_overview['Foreign Born population'] = self.helper('Foreign Born population', 'population')
		data_overview['Moved From a Different State in the Last Year'] = self.helper('Moved From a Different State in the Last Year', 'population')
		data_overview['Veterans in State'] = self.helper('Veterans in State', 'population')
		self.population_data.append(data_overview)


	# ------------------------------------
	# gets various data based on income
	# ------------------------------------
	def income_and_poverty(self):
		data_overview = {
			'Median Household Income' : '',
			'Number of people in poverty' : ''
		}
		
		data_overview['Median Household Income'] = self.helper('Median Household Income', 'income')
		data_overview['Number of people in poverty'] = self.helper('Number of people in poverty', 'income')
		self.income_data.append(data_overview)


	# ------------------------------------
	# gets various data based on education
	# ------------------------------------
	def education(self):
		data_overview = {
			'Bachelors or Higher': ''
		} 

		data_overview['Bachelors or Higher'] = self.helper('Bachelors or Higher', 'education')
		self.education_data.append(data_overview)


	# ------------------------------------
	# gets various data based on employment
	# ------------------------------------
	def employment(self):
		data_overview = {
			'Employment Rate' : '',
			'Mean Hours Working' : ''
		}

		data_overview['Employment Rate'] = self.helper('Employment Rate', 'employment')
		data_overview['Mean Hours Working'] = self.helper('Mean Hours Working', 'employment')
		self.employment_data.append(data_overview)


	# ------------------------------------
	# gets various data based on housing
	# ------------------------------------
	def housing(self):
		data_overview = {
			'Median Gross Rent' : '',
			'Homeownership Rate' : '',
			'Total Housing Units' : ''
		}

		data_overview['Median Gross Rent'] = self.helper('Median Gross Rent', 'housing')
		data_overview['Homeownership Rate'] = self.helper('Homeownership Rate', 'housing')
		data_overview['Total Housing Units'] = self.helper('Total Housing Units', 'housing')
		self.housing_data.append(data_overview)


	# ------------------------------------
	# gets various data based on health
	# ------------------------------------
	def health(self):
		data_overview = {
			'Disabled Population' : '',
			'Without Health Care Coverage' : '' 
		}

		data_overview['Disabled Population'] = self.helper('Disabled Population', 'health')
		data_overview['Without Health Care Coverage'] = self.helper('Without Health Care Coverage', 'health')
		self.health_data.append(data_overview)


	# ------------------------------------
	# gets various data based on economy
	# ------------------------------------
	def economy(self):
		data_overview = {
			'Total Annual Payroll' : '',
			'Total Retail Sales' : '',
			'Total Employer Establishments' : ''
		}

		data_overview['Total Annual Payroll'] = self.helper('Total Annual Payroll', 'economy')
		data_overview['Total Retail Sales'] = self.helper('Total Retail Sales', 'economy')
		data_overview['Total Employer Establishments'] = self.helper('Total Employer Establishments', 'economy')		
		self.economy_data.append(data_overview)


	# ------------------------------------
	# gets various data based on families
	# ------------------------------------
	def family(self):
		data_overview = {
			'Average Family Size' : '',	
			'Never Married' : ''
		}

		data_overview['Average Family Size'] = self.helper('Average Family Size', 'family')
		data_overview['Never Married'] = self.helper('Never Married', 'family')
		self.family_data.append(data_overview)


	# ------------------------------------
	# gets various data based on race
	# ------------------------------------
	def race(self):
		data_overview = {
			'Black or African American' : '',
			'American Indian and Alaska Native' : '',
			'Two or More Races' : '',	
			'Hispanic or Latino' : '',	
			'Some Other Race' : '',	
			'Asian' : '',	
			'Native Hawaiian and Pacific Islander' : '',	
			'White' : ''	
		}
	
		data_overview['Black or African American'] = self.helper('Black or African American', 'race')
		data_overview['American Indian and Alaska Native'] = self.helper('American Indian and Alaska Native', 'race')
		data_overview['Two or More Races'] = self.helper('Two or More Races', 'race')
		data_overview['Hispanic or Latino'] = self.helper('Hispanic or Latino', 'race')
		data_overview['Asian'] = self.helper('Asian', 'race')
		data_overview['Some Other Race'] = self.helper('Some Other Race', 'race')
		data_overview['Native Hawaiian and Pacific Islander'] = self.helper('Native Hawaiian and Pacific Islander', 'race')
		data_overview['White'] = self.helper('White', 'race')
		self.race_data.append(data_overview)


data = Census()



def test_write_cvs(data):
	with open('test.csv', mode='a') as file:
		order = ['name', 'Occupation', 'Income']
		writer = csv.DictWriter(file, fieldnames=order)
		writer.writerow(data)

def test_read_cvs():
	with open('test.csv') as file:
		keys = ['name', 'Occupation', 'Income']
		reader = csv.DictReader(file, fieldnames=keys)

		results = []
		for row in reader:
			results.append(dict(row))
		return results


def test_csv():
	t = {'name': 'Ant', 'Occupation': 'Programmer', 'Income': '85k'}
	t2 = {'name': 'Tom', 'Occupation':  'Electrician', 'Income': '70k'}	
	t3 = {'name': 'Frank', 'Occupation': 'Wielder', 'Income': '65k'}
	l = [t, t2, t3]

	for item in l:
		test_write_cvs(item)

	print(test_read_cvs())


