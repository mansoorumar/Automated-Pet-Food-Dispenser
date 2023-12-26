#!/bin/bash

cd /home/petfeeder/flasker/dispense_Update_Scripts
source ../virt/bin/activate
cd ../bluetooth_Scan
./bluetooth_Mac_Scan_Hourly.sh
