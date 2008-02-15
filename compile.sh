#!/bin/bash

# Depending on where PyBlosxom is, you might have to call this script
# like this:
#
#    PYTHONPATH=xyz ./compile.sh
#
# where "xyz" is the directory to PyBlosxom.

# rm -rf ./compiled_site/

if [[ -d ./logs/ ]]
    then echo "logs directory exists."
    else
        echo "logs directory doesn't exist--creating."
        mkdir ./logs/
fi

if [[ -d ./compiled_site/ ]]
    then
        echo "compiled_site exists, doing incremental static rendering...."
        python ./pyblosxom.cgi --static incremental
    else
        echo "compiled_site doesn't exist, doing full static rendering...."
        mkdir ./compiled_site/
        python ./pyblosxom.cgi --static
fi

cp -r ./htdocs/* ./compiled_site/
find ./compiled_site/ -name ".svn" -exec 'rm' '-rf' '{}' ';'
