#!/bin/bash

# Depending on where PyBlosxom is, you might have to call this script
# like this:
#
#    PYTHONPATH=xyz ./compile.sh
#
# where "xyz" is the directory to PyBlosxom.

if [[ -d ./logs/ ]]
then
    echo "logs directory exists."
else
    echo "logs directory doesn't exist--creating."
    mkdir ./logs/
fi

# get the latest docs
pushd ../pyblosxom/docs/ && make html && popd
cp -ar ../pyblosxom/docs/_build/html/* htdocs/1.5/

# update the registry from the pyblosxom/plugins
PYTHONPATH=../pyblosxom/ python ./update_registry.py ../pyblosxom/plugins/ ./registry/

if [[ -d ./compiled_site/ ]]
then
    echo "compiled_site exists, doing incremental static rendering...."
    # PYTHONPATH=../pyblosxom/ python ./pyblosxom.cgi staticrender --incremental
    PYTHONPATH=../pyblosxom/ python ./pyblosxom.cgi staticrender
else
    echo "compiled_site doesn't exist, doing full static rendering...."
    mkdir ./compiled_site/
    PYTHONPATH=../pyblosxom/ python ./pyblosxom.cgi staticrender
fi

# copies over all the bits from htdocs to compiled_site if they aren't
# already there
rsync -av --filter "- .svn" ./htdocs/ ./compiled_site/
