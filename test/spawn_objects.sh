#!/bin/bash

cp ../src/Important.py .
sed -i 's/debug = False/debug = True/' ../src/Important.py

python3 ../src/Pacthon.py
cp Important.py ../src/Important.py
rm Important.py
