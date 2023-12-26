import pandas as pd
from datetime import datetime
import subprocess

# Reading the manual dispense excel spreadsheet
manualFile_path = '/home/petfeeder/flasker/manual_dispense_times.xlsx'
sheet_name = 'Sheet1'
df_manualExcel = pd.read_excel(manualFile_path, sheet_name=sheet_name)

# Grabbing the current time and formatting it correctly
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

# Creating a new dataframe to append to the manual dispense spreadsheet
df_append = pd.DataFrame({'Time': [current_time], 'Dispensed': ['Food Dispensed']})
	
# Append the dataframe over the pre-existing one and save it to another variable
df_updated = df_manualExcel.append(df_append)

# Checking the dispenser config for the max feed amount
configFile_path = '/home/petfeeder/flasker/dispenser_Config.xlsx'
df_config = pd.read_excel(configFile_path, sheet_name=sheet_name)

feedAmount = df_config.values[0][2]

if feedAmount == 1:
	motorDispenseCommand = "cd /home/petfeeder/flasker/dispense_Update_Scripts && python3 motor_Dispense_" + str(feedAmount) + ".py"
	print(subprocess.run([motorDispenseCommand], shell=True))

elif feedAmount == 2:
	motorDispenseCommand = "cd /home/petfeeder/flasker/dispense_Update_Scripts && python3 motor_Dispense_" + str(feedAmount) + ".py"
	print(subprocess.run([motorDispenseCommand], shell=True))

elif feedAmount == 3:
	motorDispenseCommand = "cd /home/petfeeder/flasker/dispense_Update_Scripts && python3 motor_Dispense_" + str(feedAmount) + ".py"
	print(subprocess.run([motorDispenseCommand], shell=True))  

# Overwrite the excel file with the new dataframe
writer = pd.ExcelWriter(manualFile_path, engine='xlsxwriter')
df_updated.to_excel(writer, sheet_name=sheet_name, index=False)
writer.close()

