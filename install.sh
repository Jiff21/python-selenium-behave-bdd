#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT=$(dirname ${DIR})
requiredver="3.4"
first_untested_python='3.8.2'



# Python version checks
python3ver="$(python3 --version | tr -d 'Python ')"
if ! [ -x "$(command -v python3 --version )" ]; then
  echo 'Python 3 not installed' >&2
  exit 1
fi

# Check Python is new enough
if [ "$(printf '%s\n' "$requiredver" "$python3ver" | sort -V | head -n1)" = "$requiredver" ]; then
  echo "User has Python $python3ver, which meets > $requiredver requirement."
else
  echo "Less than $requiredver"
  exit 1
fi
# Warn if Pythhon is newer than tested
if [ "$(printf '%s\n' "$first_untested_python" "$python3ver" | sort -V | head -n1)" = "$first_untested_python" ]; then
  printf "\n\nWARNING:Has not been tested above Python $first_untested_python may or may not work.\n\n'."
fi
# Check virtualenv installed
if ! [ -x "$(command -v virtualenv --version)" ]; then
  printf 'virtualenv is not installed.\Running pip3 install virtualenv.\n'
  pip3 install virtualenv
fi

if [[ -d env ]]; then
  echo "virtualenv exists checking version"
  source env/bin/activate
  env_python="$(python --version)"
  if [ "$(printf '%s\n' "$requiredver" "$env_python" | sort -V | head -n1)" = "$requiredver" ]; then
    echo "Existing virtualenv using Python $env_python, meets > $requiredver requirement."
  else
    echo "Less than $requiredver"
    exit 1
  fi
else
  echo "creating virtualenv"
  virtualenv -p python3 env
  source env/bin/activate
fi


./utilities/driver_update/geckodriver.sh
./utilities/driver_update/chromedriver.sh
pip3 install -U -r requirements.txt
source env/bin/activate
