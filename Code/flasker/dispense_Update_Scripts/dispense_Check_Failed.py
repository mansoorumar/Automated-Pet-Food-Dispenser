import pandas as pd
from datetime import datetime

# Converting the daily schedule into a pandas dataframe
dailyFile_path = '/home/petfeeder/flasker/daily_dispense_schedule.xlsx'
sheet_name = 'Sheet1'
df_dailyExcel = pd.read_excel(dailyFile_path, sheet_name=sheet_name)

# Convert the database into an array to sift through list for time
df_dailyExcel_Array = df_dailyExcel.values

# Take current time and find which index contains the time
current_time = datetime.now().replace(microsecond=0, second=0, minute=0).strftime("%H:%M:%S")

index = 0

for i, item in enumerate(df_dailyExcel_Array):
    time_str = str(item[0])
    if time_str == current_time:
        index = i

# Use the Index to say that the Food is Dispensed
df_dailyExcel.at[index, 'Dispensed'] = "Pet Not Nearby"

# Write the changes back to the file
writer = pd.ExcelWriter(dailyFile_path, engine='xlsxwriter')
df_dailyExcel.to_excel(writer, sheet_name=sheet_name, index=False)
writer.close()

