import xpaths
import states

import pprint
from time import sleep
from selenium import webdriver

class Census():
	def __init__(self):
		
		self.states = states.data
		self.xpath_overview = xpaths.data
		self.pp = pprint.PrettyPrinter(indent=4)
		
		self.browser = webdriver.Chrome(executable_path=r"chromedriver.exe")

		self.data_overview = {
			'total_population' : '',
			'employment_rate' : '',
			'total_households' : '',
			'total_housing_units' : '',
			'median_household_income' : '',
			'bachelor_degree_or_higher' : '',
			'without_health_care_coverage' : '',
			'total_employer_establishments' : ''
		}

		self.overview()

	def overview(self):
		self.browser.get(self.states['Missouri'])
		sleep(10)

		self.data_overview['employment_rate'] = self.browser.find_elements_by_xpath(self.xpath_overview['employment_rate'])[0].text
		self.data_overview['total_population'] = self.browser.find_elements_by_xpath(self.xpath_overview['total_population'])[0].text
		self.data_overview['total_households'] = self.browser.find_elements_by_xpath(self.xpath_overview['total_households'])[0].text
		self.data_overview['total_housing_units'] = self.browser.find_elements_by_xpath(self.xpath_overview['total_housing_units'])[0].text
		self.data_overview['median_household_income'] = self.browser.find_elements_by_xpath(self.xpath_overview['median_household_income'])[0].text
		self.data_overview['bachelor_degree_or_higher'] = self.browser.find_elements_by_xpath(self.xpath_overview['bachelor_degree_or_higher'])[0].text
		self.data_overview['without_health_care_coverage'] = self.browser.find_elements_by_xpath(self.xpath_overview['without_health_care_coverage'])[0].text
		self.data_overview['total_employer_establishments'] = self.browser.find_elements_by_xpath(self.xpath_overview['total_employer_establishments'])[0].text
	
		self.pp.pprint(self.data_overview)

	def populations_and_people():
		pass

	def income_and_poverty():
		pass

	def education():
		pass

	def employment():
		pass

	def housing():
		pass

	def health():
		pass

	def business_and_economy():
		pass

	def families_and_living_arrangements():
		pass

	def race_and_ethnicity():
		pass



data = Census()