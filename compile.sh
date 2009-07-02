#!/bin/bash

# Depending on where PyBlosxom is, you might have to call this script
# like this:
#
#    PYTHONPATH=xyz ./compile.sh
#
# where "xyz" is the directory to PyBlosxom.

if [[ -d ./logs/ ]]
    then echo "logs directory exists."
    else
        echo "logs directory doesn't exist--creating."
        mkdir ./logs/
fi

if [[ -d ./compiled_site/ ]]
    then
        echo "compiled_site exists, doing incremental static rendering...."
        python ./pyblosxom.cgi staticrender --incremental
    else
        echo "compiled_site doesn't exist, doing full static rendering...."
        mkdir ./compiled_site/
        python ./pyblosxom.cgi staticrender
fi

# copies over all the bits from htdocs to compiled_site if they aren't
# already there
rsync -av --filter "- .svn" ./htdocs/ ./compiled_site/
