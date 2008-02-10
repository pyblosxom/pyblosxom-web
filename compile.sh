#!/bin/bash

# Depending on where PyBlosxom is, you might have to call this script
# like this:
#
#    PYTHONPATH=xyz ./compile.sh
#
# where "xyz" is the directory to PyBlosxom.

rm -rf ./compiled_site/
rm -rf ./logs/

python ./pyblosxom.cgi --static

cp -r ./htdocs/* ./compiled_site/
