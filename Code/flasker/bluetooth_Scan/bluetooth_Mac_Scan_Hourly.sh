#!/bin/bash

cd /home/petfeeder/flasker/bluetooth_Scan
> ble_Mac_Addresses.txt
sudo timeout -s SIGINT 5s hcitool -i hci0 lescan > ble_Mac_Addresses.txt
source ../virt/bin/activate
tag_Found=$(python3 tag_Check.py)

if [ "$tag_Found" == "True" ] ; then
	cd /home/petfeeder/flasker/dispense_Update_Scripts
	python3 dispense_Check_Passed.py
else
	cd /home/petfeeder/flasker/dispense_Update_Scripts
	python3 dispense_Check_Failed.py
fi
