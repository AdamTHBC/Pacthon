#!/bin/bash

cp ../src/Important.py .
sed -i 's/amountItem = 10/amountItem = 1/' ../src/Important.py
sed -i 's/amountGold = 10/amountGold = 1/' ../src/Important.py
sed -i 's/amountMonster = 10/amountMonster = 1/' ../src/Important.py
sed -i 's/max_x = 20/max_x = 3/' ../src/Important.py
sed -i 's/max_y = 10/max_y = 3/' ../src/Important.py

python3 ../src/Pacthon.py
cp Important.py ../src/Important.py
rm Important.py