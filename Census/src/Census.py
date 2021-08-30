import xpaths
import states

import json
import pprint
from time import sleep
from selenium import webdriver

class Census():
	def __init__(self):
		self.states = states.data
		self.pp = pprint.PrettyPrinter(indent = 4)
		self.browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
		
		self.data_collection = {} # collection of all the data
		self.state_data = {} # all data from all states
		self.navigate()

	def print_data(self):
		self.pp.pprint(self.state_data)


	# ------------------------------------
	#	visits the url for each state
	# ------------------------------------
	def write_dictionary(self):
		with open('census_data.txt', 'w') as convert_file:
			convert_file.write(json.dumps(self.state_data))

	# ------------------------------------
	#	visits the url for each state
	# ------------------------------------
	def navigate(self):
		sleep(3)

		for key in self.states:
			self.browser.get(self.states[key])
			sleep(10)

			# populate the current state array with the extracted data
			self.data_collection['overview'] = self.overview()
			self.data_collection['population'] = self.populations_and_people()
			self.data_collection['income'] = self.income_and_poverty()
			self.data_collection['education'] = self.education()
			self.data_collection['employment'] = self.employment()
			self.data_collection['housing'] = self.housing()
			self.data_collection['health'] = self.health()
			self.data_collection['economy'] = self.economy()
			self.data_collection['family'] = self.family()
			self.data_collection['race'] = self.race()
			self.state_data[key] = self.data_collection
			self.data_collection = {}
			sleep(2)

		self.write_dictionary()
			
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
		return data_overview
		

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
		return data_overview


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
		return data_overview


	# ------------------------------------
	# gets various data based on education
	# ------------------------------------
	def education(self):
		data_overview = {
			'Bachelors or Higher': ''
		} 

		data_overview['Bachelors or Higher'] = self.helper('Bachelors or Higher', 'education')
		return data_overview


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
		return data_overview


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
		return data_overview


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
		return data_overview


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
		return data_overview


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
		return data_overview


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
		return data_overview


# run
data = Census()