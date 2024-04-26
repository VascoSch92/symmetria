#!/bin/bash

# Check if the '--report' flag is provided
if [[ "$@" == *"--report"* ]]; then
    pytest --cov=symmetria --cov-report term-missing --cov-report html
else
    pytest --cov=symmetria --cov-report term-missing
fi
