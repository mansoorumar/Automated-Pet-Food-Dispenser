from flask import Flask, render_template, request
from datetime import datetime
import pandas as pd
import subprocess

# Create the Flask Instance
app = Flask(__name__)

# Create a web homepage
@app.route('/', methods=['GET', 'POST'])
def index():

	# Handling manual dispense database
	if request.form.get('manualDispense') == None:
		manualDispense = 0

	else:
		# Run code that appends to the manual dispense database
		print(subprocess.run(["/home/petfeeder/flasker/bluetooth_Scan/bluetooth_Mac_Scan.sh"], shell=True))

	dailyFile_path = '/home/petfeeder/flasker/daily_dispense_schedule.xlsx'
	manualFile_path = '/home/petfeeder/flasker/manual_dispense_times.xlsx'
	sheet_name = 'Sheet1'

	# Read the excel files that I require
	df_dailyExcel = pd.read_excel(dailyFile_path, sheet_name=sheet_name)
	df_manualExcel = pd.read_excel(manualFile_path, sheet_name=sheet_name)

	# Convert the excel file to an html file that I can pass through to the webpage
	# classes adds the css for the nice look, index=False removes index values, justify="center" centers the first row
	# the .replace function is meant to replace the generated code to include a center text attribute as well for the other rows
	df_daily_html = (df_dailyExcel.to_html(classes="table table-striped", index=False, justify="center", na_rep='Not Dispensed').replace('<td>', '<td align="center">'))
	df_manual_html = (df_manualExcel.to_html(classes="table table-striped", index=False, justify="center", na_rep='Not Dispensed').replace('<td>', '<td align="center">'))


	return render_template('index.html', df_daily_html=df_daily_html, df_manual_html=df_manual_html)

	
# Creating the setup webpage
@app.route('/setup')
def setup():
	return render_template('setup.html')
	

# Creating Results webpage
@app.route('/results', methods=['POST'])
def dispenserData():
	feedInterval = int(request.form.get('feedInterval'))
	maxFeedQuota = int(request.form.get('maxFeedQuota'))
	feedAmount = request.form.get('feedAmount')

	if feedAmount == "A Little Amount of Food":
		feedAmountDataFrame = 1
	elif feedAmount == "A Moderate Amount of Food":
		feedAmountDataFrame = 2
	elif feedAmount == "A Heavy Amount of Food":
		feedAmountDataFrame = 3

	# Update the dailyFeedSchedule using bash script
	# run the bash script with the feedInterval passed as an argument, that argument selects the template to copy
	updatedScheduleCommand = "/home/petfeeder/flasker/dispense_Update_Scripts/scheduleUpdate.sh " + str(feedInterval)
	print(subprocess.run([updatedScheduleCommand], shell=True))

	
	# User Data stored in dataframe
	df = pd.DataFrame({'feedInterval': [feedInterval], 'maxFeedQuota': [maxFeedQuota], 'feedAmount': [feedAmountDataFrame], 'todayFeedCount': [0]})
	
	# Provide the full file path to the excel_database.xlsx
	file_path = '/home/petfeeder/flasker/dispenser_Config.xlsx'
	sheet_name = 'Sheet1'

	# Load excel file 
	df_excel = pd.read_excel(file_path, sheet_name=sheet_name)

	# Update the file dataframe with our new user values
	df_excel.update(df)
	
	# Write the updated dataframe to the excel file
	writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
	df_excel.to_excel(writer, sheet_name=sheet_name, index=False)
	writer.close()

	return render_template('results.html', feedInterval=feedInterval, maxFeedQuota=maxFeedQuota, feedAmount=feedAmount)


if __name__ == '__main__':
	app.run(debug=True, host='10.0.0.124', port='5000')
