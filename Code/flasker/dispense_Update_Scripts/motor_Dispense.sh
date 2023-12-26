#!/bin/bash

cd /home/ekso/flasker/dispense_Update_Scripts
source ../virt/bin/activate
python3 motor_Dispense_$1.py
