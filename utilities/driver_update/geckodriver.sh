#!/bin/bash


LATEST_GECKODRIVER=$( curl -s -I -X GET https://github.com/mozilla/geckodriver/releases/latest |  grep -e '\location:*' | grep -Eo '[0-9]+\.[0-9]+\.[0-9]')

echo 'Downloading Geckodriver ' $LATEST_GECKODRIVER
if [ "$(uname)" == "Darwin" ]; then
  echo 'on OSX 64'
  curl -L https://github.com/mozilla/geckodriver/releases/download/v$LATEST_GECKODRIVER/geckodriver-v$LATEST_GECKODRIVER-macos.tar.gz | tar xz -C env/bin
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  echo 'on Linux 64'
  curl -L https://github.com/mozilla/geckodriver/releases/download/v$LATEST_GECKODRIVER/geckodriver-v$LATEST_GECKODRIVER-linux64.tar.gz | tar xz -C env/bin
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
  echo 'on Windows 32'
  curl -L https://github.com/mozilla/geckodriver/releases/download/v$LATEST_GECKODRIVER/geckodriver-v$LATEST_GECKODRIVER-win32.zip | tar xz -C env/bin
fi
