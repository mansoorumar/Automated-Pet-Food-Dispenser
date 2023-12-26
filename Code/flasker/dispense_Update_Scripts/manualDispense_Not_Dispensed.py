import pandas as pd
from datetime import datetime

# Reading the manual dispense excel spreadsheet
manualFile_path = '/home/petfeeder/flasker/manual_dispense_times.xlsx'
sheet_name = 'Sheet1'
df_manualExcel = pd.read_excel(manualFile_path, sheet_name=sheet_name)

# Grabbing the current time and formatting it correctly
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

# Creating a new dataframe to append to the manual dispense spreadsheet
df_append = pd.DataFrame({'Time': [current_time], 'Dispensed': ['Not Dispensed']})
	
# Append the dataframe over the pre-existing one and save it to another variable
df_updated = df_manualExcel.append(df_append)

# Overwrite the excel file with the new dataframe
writer = pd.ExcelWriter(manualFile_path, engine='xlsxwriter')
df_updated.to_excel(writer, sheet_name=sheet_name, index=False)
writer.close()

