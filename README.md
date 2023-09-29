# BDD Python Selenium Behave 

## Introduction

A portfollio example of python selenium tests. I'm a big fan of Gherkin Syntax and Behave is one of my favorite tools to write BDD Tests. The feature files give people context to what is expected and how it failed faster than if they needed to go read all the test functions to catch up on how the test is setting up and what it expected.

See [products.feature](/features/products.feature) or any of the other [feature files](/features), to get an idea how easy figure out what's going on. If you're unfamiliar with behaves folder structure go to the [steps directory](/features/steps) for code samples.

I used a variety of differing selectors, interaction methods & waits to demonstrate my knowledge of selenium. I chose to write the tests against a saucelabs demo site to minimize maintenace, but does limit what I have to test in a way where not everythning I can do wil be on display in this demo. 

## Install

### Dependancies

* [Python 3](https://www.python.org/downloads/).
* Virtualenv (`pip3 install virtualenv`).

### Install steps

```bash
virtualenv -p python3.6 env
source env/bin/activate
./utilities/driver_update/geckodriver.sh
./utilities/driver_update/chromedriver.sh
pip3 install -U -r requirements.txt
```

Or just run `./install.sh`

## Running Tests

```bash
behave features
```

## Allure reports

For a prettier report checkout [Allure](https://docs.qameta.io/allure/) reports with the steps below.

### Install

```bash
pip3 install -U -r utilities/allure/requirements.txt
brew install allure
```

### Run

```bash
behave -f allure_behave.formatter:AllureFormatter -o utilities/allure/allure_results ./features
```

### Generate and run reports.

```bash
allure generate utilities/allure/allure_results/ -o utilities/allure/allure-reports/ --clean
allure open utilities/allure/allure-reports/
```


If you want a History section next time you run, you need to copy the history from the previous report, before generating the next report.

```bash
rm -R utilities/allure/allure_results/*
cp -R utilities/allure/allure-reports/history/ utilities/allure/allure_results/history
```