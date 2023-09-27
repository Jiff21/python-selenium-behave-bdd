#!/bin/sh

echo 'Copying or adding qa .gitignores into the root project'
cat .gitignore >> .gitignore
echo 'Copying or adding qa Makefile into the root project'
cat Makefile >> Makefile
echo 'Only run this command once its not smart and will double these.'
