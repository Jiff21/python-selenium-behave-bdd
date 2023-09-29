# QA Stack

* Behave ([Unit, End-to-End](/functional), and [Analytics](/analytics) tests)
* [Locust](/performance) (Performance tests)
* [Lighthouse](/accessibility) (Accessibility & Mobile Support)


## Introduction


## Install

### Dependancies

Install [python 3](https://www.python.org/downloads/) and
[Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac)
using their .dmg files. Written at Python 3.6.1 for OSX. Virtualenv (`pip3 install virtualenv`).

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
