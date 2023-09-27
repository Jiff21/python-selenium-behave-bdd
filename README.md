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

Local install is below, but if you want a demo skip to [Run All Tests](#run-all-tests).

```bash
virtualenv -p python3.6 env
source env/bin/activate
./utilities/driver_update/geckodriver.sh
./utilities/driver_update/chromedriver.sh
pip3 install -U -r requirements.txt
```

Edit the file settings.py to match your development setup (localhost,
HOST_URL, Selenium Server, etc) if you're using this for another site.


## Running Tests

```bash

```

```bash
pip3 install -U -r utilities/allure/requirements.txt
allure generate utilities/allure/allure_results/ -o utilities/allure/allure-reports/ --clean
allure open utilities/allure/allure-reports/
```

See [Allure](/utilities/allure) for more on allure results and generating
history / trends.

### Extras

#### Service Account Authentication and Identity Aware Proxy (Optional)
If your development environment is protected by IAP, there is a setup for a service account
and a chrome that loads an extension that adds Bearer tokens to the header. Follow
[mod_header utility setup](utilities/oauth) instructions. Then change browser imports in
the feature/environment.py files for analytics and functional to
```from functional.features.auth_browser import Browser```.

```bash
pip3 install -U -r utilities/oauth/requirements.txt
export CLIENT_ID='########-ksdbjsdkg3893gsbdoi-apps.googleusercontent.com'
export GOOGLE_APPLICATION_CREDENTIALS='path/to/json_token.json'
```

#### [<sup>1</sup>] Pipeline Variables

The necessary pipeline variables depend on what you're using from this scaffolding.  
If you want to use functional/steps/login.py you need to setup all the account variables.
If you end up send allure reports be sure to add ALLURE_REPORT_HUB_URL, ALLURE_PROJECT_NAME,
ALLURE_HUB_CLIENT_ID. If you're using the Google IAP OATH tool above be sure to set up
CLIENT_ID and GOOGLE_APPLICATION_CREDENTIALS, you past in the content of the file for the
value instead of a path like you use locally.


#### Setting Local Environment Variables (Optional)

Duplicate the file found at secrets/example.env.example and rename it `testing.env`,
`staging.env`, `dev.env`, or `production.env`. Edit the values in that file to match
you environment or in `settings.py` to edit the default/local environment values.
You can now switch between environments while testing by setting a `QA_ENV` variable
(for example `export QA_ENV=testing`).

Or variables for IAP or using a remote allure hub. You also want to add these
as secret variables on your CI env if you plan on running similar tests on CI.
The demo tests in this project should all run off the defaults set in
settings.py.

---

If you plan to integrate this into CI, you obviously add commands & environment
variables[<sup>1</sup>](#1-pipeline-variables) to your projects
docker-compose.yml, .gitlab-ci.yml or bitbucket-pipelines.yml. There are example
CI implementation files in ci_files.
