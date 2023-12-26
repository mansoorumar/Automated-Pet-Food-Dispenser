#!/bin/bash

#cd /home/petfeeder/flasker/bluetooth_Scan
#> ble_Mac_Addresses.txt
#sudo timeout -s SIGINT 5s hcitool -i hci0 lescan > ble_Mac_Addresses.txt
#tag_Found=$(python3 tag_Check.py)

#if [ "$tag_Found" == "True" ] ; then
#	cd /home/petfeeder/flasker/dispense_Update_Scripts
#	python3 manualDispense_Food_Dispensed.py
#else
#	cd /home/petfeeder/flasker/dispense_Update_Scripts
#	python3 manualDispense_Not_Dispensed.py
#fi

cd /home/petfeeder/flasker/dispense_Update_Scripts
source ../virt/bin/activate
python3 manualDispense_Food_Dispensed.py
