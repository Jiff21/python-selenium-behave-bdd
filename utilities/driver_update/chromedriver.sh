#!/bin/bash

LATEST_CHROMEDRIVER=$(curl "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE")
echo 'Downloading Chromedriver ' $LATEST_CHROMEDRIVER

if [ "$(uname)" == "Darwin" ]; then
  echo 'on OSX 64'
  curl -L "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$LATEST_CHROMEDRIVER/mac-x64/chromedriver-mac-x64.zip" | tar xz -C env/bin
  mv env/bin/chromedriver-mac-x64/chromedriver env/bin
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  echo 'on Linux 64'
  curl -L "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$LATEST_CHROMEDRIVER/linux64/chromedriver-linux64.zip" | tar xz -C env/bin
  mv env/bin/chromedriver-linux64/chromedriver env/bin
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
  echo 'on Windows 32'
  curl -L https://chromedriver.storage.googleapis.com/$LATEST_CHROMEDRIVER/chromedriver_win64.zip | tar xz -C env/bin
  mv env/bin/chromedriver_win64/chromedriver env/bin
fi

chmod +x env/bin/chromedriver