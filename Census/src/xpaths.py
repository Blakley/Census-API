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

# Population by Age Range
population_age = {
	'Median Age' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}

# Computer and Internet Use
population_tech_use = {
	'Without an Internet Subscription' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]',
}

# Language Spoken at Home
population_home_lang = {
	'Language Other Than English Spoken at Home' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[4]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}

# Native and Foreign Born
population_native_born = {
	'Foreign Born population' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[5]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}

# Residential Mobility 
population_Residential_Mobility = {
	'Moved From a Different State in the Last Year': '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[6]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}

# Veterans
population_veterans = {
	'Veterans in State': '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[1]/div/div[7]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}


# --------------------------------------------------------------------------------------------
# 									Income and Poverty
# --------------------------------------------------------------------------------------------

# Median Household Income
income_median = {
	'Median Household Income' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[2]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}

# Poverty, All people in Location
income_poverty = {
	'Number of people in poverty' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}


# --------------------------------------------------------------------------------------------
# 									Education
# --------------------------------------------------------------------------------------------

# Educational Attainment
education_bachelors = {
	'Bachelors or Higher': '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[3]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
} 


# --------------------------------------------------------------------------------------------
# 									Employment
# --------------------------------------------------------------------------------------------


# Employment and Labor Force Status
employment_rate = {
	'Employment Rate' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[4]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}

# Work Experience
employment_work_hours = {
	'Mean Hours Working' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[4]/div/div[6]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}


# --------------------------------------------------------------------------------------------
# 									Housing
# --------------------------------------------------------------------------------------------

# Financial Characteristics
housing_gross_rent = {
	'Median Gross Rent' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[5]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}

# Homeownership Rate
housing_ownership = {
	'Homeownership Rate' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[5]/div/div[2]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}

# Housing Units
housing_units = {
	'Total Housing Units' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[5]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}


# --------------------------------------------------------------------------------------------
# 									Health
# --------------------------------------------------------------------------------------------

# Disability
health_disability = {
	'Disabled Population' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[6]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}

# Health Insurance
health_insurance = {
	'Without Health Care Coverage' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[6]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]' 
}



# --------------------------------------------------------------------------------------------
# 									Business and Economy
# --------------------------------------------------------------------------------------------

# Expenses and Expenditures
economy_payroll = {
	'Total Annual Payroll' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[7]/div/div[2]/div[1]/div/div[1]/div[1]/div/p[1]/span'
}

# Sales, Shipments, and Production
economy_retail_sales = {
	'Total Retail Sales' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[7]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span'	
}

# Small Business
economy_small_business = {
	'Total Employer Establishments' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[7]/div/div[4]/div[1]/div/div[1]/div[1]/div/p[1]/span'
}


# --------------------------------------------------------------------------------------------
# 									Families and Living Arrangements
# --------------------------------------------------------------------------------------------

# Families and Household Characteristics
family_avg_size = {
	'Average Family Size' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[8]/div/div[2]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'	
}

# Marital Status and Marital History
family_never_married = {
	'Never Married' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[8]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}


# --------------------------------------------------------------------------------------------
# 									Race and Ethnicity
# --------------------------------------------------------------------------------------------

# Black or African American
race_black = {
	'Black or African American' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[3]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'	
}

# American Indian and Alaska Native
race_american_indian = {
	'American Indian and Alaska Native' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[1]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'
}

# Two or More Races
race_mixed = {
	'Two or More Races' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[8]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'	
}

# Hispanic or Latino
race_hispanic = {
	'Hispanic or Latino' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[4]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'	
} 

# Some Other Race
race_other = {
	'Some Other Race' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[7]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'	
}

# Asian
race_asian = {
	'Asian' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[2]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'	
}

# Native Hawaiian and Pacific Islander
race_hawaiian = {
	'Native Hawaiian and Pacific Islander' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[5]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'	
}

# White
race_white = {
	'White' : '//*[@id="app-layout"]/div[3]/div/div[2]/main/div/div/div/div[2]/section[9]/div/div[9]/div[1]/div/div[1]/div[1]/div/p[1]/span[1]'	
}