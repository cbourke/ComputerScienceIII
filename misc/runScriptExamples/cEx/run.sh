#!/bin/bash

#if the executable hello does not already exist, compile it
if ! [ -a hello ]; then
    gcc -o hello hello.c
fi

# run the executable, passing command line arguments
./hello "$@"

