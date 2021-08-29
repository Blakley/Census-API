# --------------------------------------------------------------------------------------------
# 									state overview
# --------------------------------------------------------------------------------------------

data =  {
	'total_population' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[1]/div[3]/div[1]/div[3]',
	'employment_rate' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[1]/div[3]/div[4]/div[3]',
	'total_households' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[1]/div[3]/div[8]/div[3]',
	'total_housing_units' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[1]/div[3]/div[5]/div[3]',
	'median_household_income' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[1]/div[3]/div[2]/div[3]',
	'bachelor_degree_or_higher' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[1]/div[3]/div[3]/div[3]',
	'without_health_care_coverage' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[1]/div[3]/div[6]/div[3]',
	'total_employer_establishments' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[1]/div[3]/div[7]/div[3]'
}


# --------------------------------------------------------------------------------------------
# 									Populations and People
# --------------------------------------------------------------------------------------------

population = {
	# Median Age
	'Median Age' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# Computer and Internet Use
	'Without an Internet Subscription': '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# Language Spoken at Home
	'Language Other Than English Spoken at Home' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[4]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# Native and Foreign Born
	'Foreign Born population' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[5]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# Residential Mobility 
	'Moved From a Different State in the Last Year' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[6]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# Veterans
	'Veterans in State' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[7]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}

# --------------------------------------------------------------------------------------------
# 									Income and Poverty
# --------------------------------------------------------------------------------------------


income = {
	# Median Household Income
	'Median Household Income' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[2]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# Poverty, All people in Location
	'Number of people in poverty' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'

}

# --------------------------------------------------------------------------------------------
# 									Education
# --------------------------------------------------------------------------------------------

# Educational Attainment
education = {
	'Bachelors or Higher': '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[3]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
} 


# --------------------------------------------------------------------------------------------
# 									Employment
# --------------------------------------------------------------------------------------------

employment = {
	# Employment and Labor Force Status
	'Employment Rate' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[4]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# Work Experience
	'Mean Hours Working' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[4]/div/div[6]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'

}


# --------------------------------------------------------------------------------------------
# 									Housing
# --------------------------------------------------------------------------------------------


housing = {
	# Financial Characteristics
	'Median Gross Rent' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[5]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# Homeownership Rate
	'Homeownership Rate' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[5]/div/div[2]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# Housing Units
	'Total Housing Units' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[5]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}



# --------------------------------------------------------------------------------------------
# 									Health
# --------------------------------------------------------------------------------------------

health = {
	# Disability
	'Disabled Population' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[6]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# Health Insurance
	'Without Health Care Coverage' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[6]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]' 

}


# --------------------------------------------------------------------------------------------
# 									Business and Economy
# --------------------------------------------------------------------------------------------

economy = {
	# Expenses and Expenditures
	'Total Annual Payroll' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[7]/div/div[2]/div[1]/div/div[1]/div[1]/div/p[1]/span',
	# Sales, Shipments, and Production
	'Total Retail Sales' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[7]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span',
	# Small Business
	'Total Employer Establishments' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[7]/div/div[4]/div[1]/div/div[1]/div[1]/div/p[1]/span'
}


# --------------------------------------------------------------------------------------------
# 									Families and Living Arrangements
# --------------------------------------------------------------------------------------------


family = {
	# Families and Household Characteristics
	'Average Family Size' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[8]/div/div[2]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',	
	# Marital Status and Marital History
	'Never Married' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[8]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}


# --------------------------------------------------------------------------------------------
# 									Race and Ethnicity
# --------------------------------------------------------------------------------------------

race = {
	# Black or African American
	'Black or African American' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# American Indian and Alaska Native
	'American Indian and Alaska Native' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
	# Two or More Races
	'Two or More Races' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[8]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',	
	# Hispanic or Latino
	'Hispanic or Latino' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[4]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',	
	# Some Other Race
	'Some Other Race' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[7]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',	
	# Asian
	'Asian' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[2]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',	
	# Native Hawaiian and Pacific Islander
	'Native Hawaiian and Pacific Islander' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[5]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',	
	# White
	'White' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[9]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'	
}


