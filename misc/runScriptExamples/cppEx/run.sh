#!/bin/bash

#if the executable hello does not already exist, compile it
if ! [ -a hello ]; then
    g++ -o hello hello.cpp
fi

# run the executable, passing command line arguments
./hello "$@"

