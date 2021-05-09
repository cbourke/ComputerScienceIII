#!/bin/bash

#if the executable hello does not already exist, compile it
if ! [ -a hello ]; then
    rustc -o helll hello.rs
fi

# run the executable, passing command line arguments
./hello "$@"

