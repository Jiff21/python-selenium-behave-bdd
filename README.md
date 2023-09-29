# BDD Python Selenoum Behave 

## Introduction

A portfollio example of python selenium tests. I'm a big fan of Gherkin Syntax and Behave is one of my favorite tools to write BDD Tests. I tried to use a variety of differing selectors, interaction methods & waits to demonstrate my knowledge of selenium. I used a demo saucelaps site to minimize maintenace for my demo, but does limit how many tests I should write. 

## Install

### Dependancies

* [python 3](https://www.python.org/downloads/).
* Virtualenv (`pip3 install virtualenv`).

### Install steps

```bash
virtualenv -p python3.6 env
source env/bin/activate
./utilities/driver_update/geckodriver.sh
./utilities/driver_update/chromedriver.sh
pip3 install -U -r requirements.txt
```

## Running Tests

```bash
behave functional/features
```


# Create allure reports

```bash
pip3 install -U -r utilities/allure/requirements.txt
allure generate utilities/allure/allure_results/ -o utilities/allure/allure-reports/ --clean
allure open utilities/allure/allure-reports/
```

See [Allure](/utilities/allure) for more on allure results and generating
history / trends.
