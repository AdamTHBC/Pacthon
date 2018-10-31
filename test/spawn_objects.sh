#!/bin/bash

cp ../src/Important.py Important_original
sed -i 's/debug = False/debug = True/' ../src/Important.py

python3 ../src/Pacthon.py
cp Important_original ../src/Important.py && rm Important_original