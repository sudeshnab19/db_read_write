import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('sample.xlsx', sheet_name='Sheet')  # Replace 'Sheet1' with the actual sheet name

# Print the DataFrame
print(df)