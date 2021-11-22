#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
else 
  python3 analyze.py "$@" 
fi

