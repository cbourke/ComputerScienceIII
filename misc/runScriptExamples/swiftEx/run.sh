#!/bin/bash

#if the executable hello does not already exist, compile it
if ! [ -a hello ]; then
    swiftc -o hello hello.swift
fi

# run the executable, passing command line arguments
./hello "$@"

