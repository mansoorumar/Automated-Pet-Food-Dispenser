with open('ble_Mac_Addresses.txt') as file:
    if 'FF:FF:10:7F:25:C9' in file.read():
        print("True")
    else:
        print("False")
