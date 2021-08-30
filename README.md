# United States 2020 Census API
An unofficial API for various US 2020 Census data

## File Information
`census.py` 
Created a [selenium](https://selenium-python.readthedocs.io/) webscraper using the usa 2020 census from [census.gov](census.gov/data)

`census_dictionary.py`
A python dictionary of the extracted census values for each state

`server.py`
Created a local API on `localhost:5000` for accessing the data for each state 

`states.py`
A list of urls for each state on [census.gov](census.gov/data)

`xpaths.py`
xpath values for various elements used for accessing data on the census webpage

## Routes
API routes where `name` is the name of a state.
Note: the first letter must be capitalized. Example: Alabama

* return all the data for the state: `/state?=name` 
* get an overview of data for the state `/overview?=name`
* get the population data for the state `/population?=name`
* get the income data for the state `/income?=name`
* get the education data for the state `/education?=name`
* get the employment data for the state `/employment?=name`
* get the housing data for the state `/housing?=name`
* get the health data for the state `/health?=name`
* get the economy data for the state `/economy?=name`
* get the family data for the state `/family?=name`
* get the race data for the state `/race?=name`


## Dependencies
Download [ChromeDriver](https://chromedriver.chromium.org/downloads) and replace chromedriver.exe with the version that matches your chrome version

install the following using pip
```
$ pip install selenium
$ pip install flask
$ pip install pprintpp
```

## Deployment
To test out the webscraper run the following
```
$ python census.py
```

To simply use the API run the following 
```
$ python server.py
```


