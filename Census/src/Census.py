import xpaths
import states

import pprint
from time import sleep
from selenium import webdriver

class Census():
	def __init__(self):
		self.states = states.data
		self.pp = pprint.PrettyPrinter(indent=4)
		self.browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
		
		# data collection
		self.overview_data = [] # for entire country
		self.population_data = []
		self.income_data = []
		self.education_data = []
		self.employment_data = []
		self.housing_data = []
		self.health_data = []
		self.economy_data = []
		self.family_data = []
		self.race_data = []
		self.state_data = []

		self.navigate()

	# ------------------------------------
	#	visits the url for each state
	# ------------------------------------
	def navigate(self):
		for key in self.states:
			self.browser.get(self.states[key])
			sleep(10)

			# populate data all the data for the state
			self.state_data.append(self.overview_data)
			self.state_data.append(self.population_data)
			self.state_data.append(self.income_data)
			self.state_data.append(self.education_data)
			self.state_data.append(self.employment_data)
			self.state_data.append(self.housing_data)
			self.state_data.append(self.health_data)
			self.state_data.append(self.economy_data)
			self.state_data.append(self.family_data)
			self.state_data.append(self.race_data)

			
	# ------------------------------------
	#	extracts the xpath data
	# ------------------------------------
	def helper(self, value, category):
		if category == 'overview':
			return self.browser.find_elements_by_xpath(xpaths.data[value])[0].text

		# population
		if category == 'population':
			return self.browser.find_elements_by_xpath(xpaths.population_age[value])[0].text

		if category == 'tech':
			return self.browser.find_elements_by_xpath(xpaths.population_tech_use[value])[0].text

		if category == 'home_lang':
			return self.browser.find_elements_by_xpath(xpaths.population_home_lang[value])[0].text

		if category == 'foreign_born':
			return self.browser.find_elements_by_xpath(xpaths.population_native_born[value])[0].text	

		if category == 'moved_to_state':
			return self.browser.find_elements_by_xpath(xpaths.population_Residential_Mobility[value])[0].text			

		if category == 'veterans':
			return self.browser.find_elements_by_xpath(xpaths.population_veterans[value])[0].text	

		# income
		if category == 'income_median':
			return self.browser.find_elements_by_xpath(xpaths.income_median[value])[0].text			

		if category == 'income_poverty':
			return self.browser.find_elements_by_xpath(xpaths.income_poverty[value])[0].text

		# education
		if category == 'education':
			return self.browser.find_elements_by_xpath(xpaths.education_bachelors[value])[0].text

		# employment
		if category == 'employment_rate':
			return self.browser.find_elements_by_xpath(xpaths.employment_rate[value])[0].text

		if category == 'hours_working':
			return self.browser.find_elements_by_xpath(xpaths.employment_work_hours[value])[0].text

		# housing
		if category == 'housing_rent':
			return self.browser.find_elements_by_xpath(xpaths.housing_gross_rent[value])[0].text

		if category == 'housing_ownership':
			return self.browser.find_elements_by_xpath(xpaths.housing_ownership[value])[0].text

		if category == 'housing_units':
			return self.browser.find_elements_by_xpath(xpaths.housing_units[value])[0].text

		# health
		if category == 'health_disability':
			return self.browser.find_elements_by_xpath(xpaths.health_disability[value])[0].text

		if category == 'health_insurance':
			return self.browser.find_elements_by_xpath(xpaths.health_insurance[value])[0].text

		# economy
		if category == 'payroll':
			return self.browser.find_elements_by_xpath(xpaths.economy_payroll[value])[0].text

		if category == 'retail_sales':
			return self.browser.find_elements_by_xpath(xpaths.economy_retail_sales[value])[0].text

		if category == 'small_business':
			return self.browser.find_elements_by_xpath(xpaths.economy_small_business[value])[0].text

		# family
		if category == 'avg_size':
			return self.browser.find_elements_by_xpath(xpaths.family_avg_size[value])[0].text

		if category == 'never_married':
			return self.browser.find_elements_by_xpath(xpaths.family_never_married[value])[0].text

		# race
		if category == 'race_black':
			return self.browser.find_elements_by_xpath(xpaths.race_black[value])[0].text		

		if category == 'race_american_indian':
			return self.browser.find_elements_by_xpath(xpaths.race_american_indian[value])[0].text	

		if category == 'race_mixed':
			return self.browser.find_elements_by_xpath(xpaths.race_mixed[value])[0].text	

		if category == 'race_hispanic':
			return self.browser.find_elements_by_xpath(xpaths.race_hispanic[value])[0].text				

		if category == 'race_other':
			return self.browser.find_elements_by_xpath(xpaths.race_other[value])[0].text		

		if category == 'race_asian':
			return self.browser.find_elements_by_xpath(xpaths.race_asian[value])[0].text	

		if category == 'race_hawaiian':
			return self.browser.find_elements_by_xpath(xpaths.race_hawaiian[value])[0].text	

		if category == 'race_white':
			return self.browser.find_elements_by_xpath(xpaths.race_white[value])[0].text	


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
		self.pp.pprint(self.overview_data[0])


	# ------------------------------------
	#	gets various based on opulation
	# ------------------------------------
	def populations_and_people(self):
				
		def age_and_sex():
			population_age = { 'Median Age' : '' }	
			population_age['Median Age'] = self.helper('Median Age', 'population')
			self.population_data.append(population_age)

		def comp_and_internet_use():
			population_tech_use = { 'Without an Internet Subscription' : ''}
			population_tech_use['Without an Internet Subscription'] = self.helper('Without an Internet Subscription', 'tech')
			self.population_data.append(population_tech_use)

		def home_language():
			population_home_lang = { 'Language Other Than English Spoken at Home' : ''}
			population_home_lang['Language Other Than English Spoken at Home'] = self.helper('Language Other Than English Spoken at Home', 'home_lang')
			self.population_data.append(population_home_lang)

		def foreign_born():
			population_foreign_born = { 'Foreign Born population' : ''}
			population_foreign_born['Foreign Born population'] = self.helper('Foreign Born population', 'foreign_born')
			self.population_data.append(population_foreign_born)

		def moved_to_state():
			population_Residential_Mobility = { 'Moved From a Different State in the Last Year' : ''}
			population_Residential_Mobility['Moved From a Different State in the Last Year'] = self.helper('Moved From a Different State in the Last Year', 'moved_to_state')
			self.population_data.append(population_Residential_Mobility)

		def veterans_amount():
			population_veterans = { 'Veterans in State' : ''}
			population_veterans['Veterans in State'] = self.helper('Veterans in State', 'veterans')
			self.population_data.append(population_veterans)


	# ------------------------------------
	# gets various data based on income
	# ------------------------------------
	def income_and_poverty(self):
		def median_income():
			income_median = { 'Median Household Income' : ''}
			income_median['Median Household Income'] = self.helper('Median Household Income', 'income_median')
			self.income_data.append(income_median)

		def poverty():
			income_poverty= { 'Number of people in poverty' : ''}
			income_poverty['Number of people in poverty'] = self.helper('Number of people in poverty', 'income_poverty')
			self.income_data.append(income_poverty)


	# ------------------------------------
	# gets various data based on education
	# ------------------------------------
	def education(self):
		def degree():
			education_bachelors= { 'Bachelors or Higher' : ''}
			education_bachelors['Bachelors or Higher'] = self.helper('Bachelors or Higher', 'education')
			self.education_data.append(education_bachelors)


	# ------------------------------------
	# gets various data based on employment
	# ------------------------------------
	def employment(self):
		def rate():
			employment_rate= { 'Employment Rate' : ''}
			employment_rate['Employment Rate'] = self.helper('Employment Rate', 'employment_rate')
			self.employment_data.append(employment_rate)

		def mean_hours():
			employment_work_hours= { 'Mean Hours Working' : ''}
			employment_work_hours['Mean Hours Working'] = self.helper('Mean Hours Working', 'hours_working')
			self.employment_data.append(employment_work_hours)


	# ------------------------------------
	# gets various data based on housing
	# ------------------------------------
	def housing(self):
		def rent():
			housing_gross_rent = {'Median Gross Rent' : ''}
			housing_gross_rent['Median Gross Rent'] = self.helper('Median Gross Rent', 'housing_rent')
			self.housing_data.append(housing_gross_rent)

		def ownership():
			housing_ownership = {'Homeownership Rate' : ''}
			housing_ownership['Homeownership Rate'] = self.helper('Homeownership Rate', 'housing_ownership')
			self.housing_data.append(housing_ownership)

		def units():
			housing_units = {'Total Housing Units' : ''}
			housing_units['Total Housing Units'] = self.helper('Total Housing Units', 'housing_units')
			self.housing_data.append(housing_units)


	# ------------------------------------
	# gets various data based on health
	# ------------------------------------
	def health(self):
		def disability():
			health_disability = {'Disabled Population' : ''}
			health_disability['Disabled Population'] = self.helper('Disabled Population', 'health_disability')
			self.health_data.append(health_disability)

		def insurance():
			health_insurance = {'Without Health Care Coverage' : ''}
			health_insurance['Without Health Care Coverage'] = self.helper('Without Health Care Coverage', 'health_insurance')
			self.health_data.append(health_insurance)


	# ------------------------------------
	# gets various data based on economy
	# ------------------------------------
	def economy(self):
		def payroll():
			economy_payroll = {'Total Annual Payroll' : ''}
			economy_payroll['Total Annual Payroll'] = self.helper('Total Annual Payroll', 'payroll')
			self.economy_data.append(economy_payroll)


		def retail():
			economy_retail_sales = {'Total Retail Sales' : ''}
			economy_retail_sales['Total Retail Sales'] = self.helper('Total Retail Sales', 'retail_sales')
			self.economy_data.append(economy_retail_sales)

		def business():
			economy_small_business = {'Total Employer Establishments' : ''}
			economy_small_business['Total Employer Establishments'] = self.helper('Total Employer Establishments', 'small_business')
			self.economy_data.append(economy_small_business)


	# ------------------------------------
	# gets various data based on families
	# ------------------------------------
	def family(self):
		def average_size():
			avg_size = {'Average Family Size' : ''}
			avg_size['Average Family Size'] = self.helper('Average Family Size', 'avg_size')
			self.family_data.append(avg_size)

		def married():
			never_married = {'Never Married' : ''}
			never_married['Never Married'] = self.helper('Never Married', 'never_married')
			self.family_data.append(never_married)


	# ------------------------------------
	# gets various data based on race
	# ------------------------------------
	def race(self):
		def black():
			race_black = {'Black or African American' : ''}
			race_black['Black or African American'] = self.helper('Black or African American', 'race_black')
			self.race_data.append(race_black)

		def american_indian():
			race_american_indian = {'American Indian and Alaska Native' : ''}
			race_american_indian['American Indian and Alaska Native'] = self.helper('American Indian and Alaska Native', 'race_american_indian')
			self.race_data.append(race_american_indian)

		def mixed():
			race_mixed = {'Two or More Races' : ''}
			race_mixed['Two or More Races'] = self.helper('Two or More Races', 'race_mixed')
			self.race_data.append(race_mixed)

		def hispanic():
			race_hispanic = {'Hispanic or Latino' : ''}
			race_hispanic['Hispanic or Latino'] = self.helper('Hispanic or Latino', 'race_hispanic')
			self.race_data.append(race_hispanic)

		def Asian():
			race_asian = {'Asian' : ''}
			race_asian['Asian'] = self.helper('Asian', 'race_asian')
			self.race_data.append(race_asian)

		def other():
			race_other = {'Some Other Race' : ''}
			race_other['Some Other Race'] = self.helper('Some Other Race', 'race_other')
			self.race_data.append(race_other)

		def hawaiian():
			race_hawaiian = {'Native Hawaiian and Pacific Islander' : ''}
			race_hawaiian['Native Hawaiian and Pacific Islander'] = self.helper('Native Hawaiian and Pacific Islander', 'race_hawaiian')
			self.race_data.append(race_hawaiian)

		def white():
			race_white = {'White' : ''}
			race_white['White'] = self.helper('White', 'race_white')
			self.race_data.append(race_white)		


data = Census()