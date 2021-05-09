#!/bin/bash


#if the executable hello does not already exist, compile it using mcs
if ! [ -a Hello.exe ]; then
    mcs Hello.cs
fi

# run using mono
mono Hello.exe "$@"

