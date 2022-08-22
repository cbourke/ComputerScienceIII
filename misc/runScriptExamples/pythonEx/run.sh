#!/bin/bash

# On the cse server, multiple versions of python
# are available and you can invoke a specific one
# if you wish.  You can use a pyenv utility to
# find the available versions.
#   pyenv versions
# lists all the installe versions and
#   pyenv which python3.7
# (for example) to list the full path to a particular
# version.  You'll likely be okay simply using python
# (which is python3 by default)
# for all of your programs as in the following example.
python hello.py "$@"
