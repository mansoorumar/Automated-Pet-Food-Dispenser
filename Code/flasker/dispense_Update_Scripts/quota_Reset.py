import pandas as pd

# Provide the full file path to the excel_database.xls
file_path = '/home/petfeeder/flasker/dispenser_Config.xlsx'
sheet_name = 'Sheet1'

# Load excel file
df_excel = pd.read_excel(file_path, sheet_name=sheet_name)

df_excel.values[0][3] = 0

# Write the updated dataframe to the excel file
writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
df_excel.to_excel(writer, sheet_name=sheet_name, index=False)
writer.close()
