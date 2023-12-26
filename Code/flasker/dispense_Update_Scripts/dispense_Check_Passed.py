import pandas as pd
from datetime import datetime
import subprocess

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
        #print(f"Index {i} contains the target time.")
        index = i

# Checking the dispenser config for the max feed amount
configFile_path = '/home/petfeeder/flasker/dispenser_Config.xlsx'
df_config = pd.read_excel(configFile_path, sheet_name=sheet_name)

maxFeedQuota = df_config.values[0][1]
feedAmount = df_config.values[0][2]
todayFeedCount = df_config.values[0][3]

if todayFeedCount < maxFeedQuota:

    if feedAmount == 1:
        motorDispenseCommand = "cd /home/petfeeder/flasker/dispense_Update_Scripts && python3 motor_Dispense_" + str(feedAmount) + ".py"
        print(subprocess.run([motorDispenseCommand], shell=True))

    elif feedAmount == 2:
        motorDispenseCommand = "cd /home/petfeeder/flasker/dispense_Update_Scripts && python3 motor_Dispense_" + str(feedAmount) + ".py"
        print(subprocess.run([motorDispenseCommand], shell=True))

    elif feedAmount == 3:
        motorDispenseCommand = "cd /home/petfeeder/flasker/dispense_Update_Scripts && python3 motor_Dispense_" + str(feedAmount) + ".py"
        print(subprocess.run([motorDispenseCommand], shell=True))  

    df_config.values[0][3] = todayFeedCount + 1
    writer = pd.ExcelWriter(configFile_path, engine='xlsxwriter')
    df_config.to_excel(writer, sheet_name=sheet_name, index=False)
    writer.close()


    # Use the Index to say that the Food is Dispensed
    df_dailyExcel.at[index, 'Dispensed'] = "Food Dispensed"

else:
    # Use index and say that pet was fed too much
    df_dailyExcel.at[index, 'Dispensed'] = "Quota Reached"


# Write the changes back to the file
writer = pd.ExcelWriter(dailyFile_path, engine='xlsxwriter')
df_dailyExcel.to_excel(writer, sheet_name=sheet_name, index=False)
writer.close()
