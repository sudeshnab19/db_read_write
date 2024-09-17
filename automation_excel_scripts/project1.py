# Read 'Retail_crosstab' sql resultset from Learning database via python using venv

import psycopg2             # Module needed to connect to DB
from openpyxl import Workbook   # Module needed to import excel workbook
import pandas as pd             # Module needed to read the data

# create workbook
wb = Workbook()
# grab the active worksheet
ws = wb.active

connection = psycopg2.connect(database="Learning", user="postgres", password="password", host="localhost", port=5432) # connection established

cursor = connection.cursor()
column_names=['Store','Week1','Week2']      # column names defined

cursor.execute(f"""SELECT                   
    *
from crosstab(
'Select
    store
    ,week           
    ,cast(sum(sales) as numeric)  
from
    store
GROUP by
    store,week
order by
    store, week','select DISTINCT week from store order by week'
)
as ({column_names[0]} character VARYING, {column_names[1]} integer, {column_names[2]} integer);""")

print(column_names)
ws.append(column_names)

# Fetch all rows from database
records = cursor.fetchall()
for record in records:
    print(record)
    ws.append(record)

# Save the file
wb.save("project1.xlsx")

# Create Chart
from openpyxl.chart import BarChart, Reference
chart = BarChart()
chart.title = "Sales by Stores"
chart.x_axis.title = "Stores"
chart.y_axis.title = "Sum of Sales"

# Add data to the chart
data = Reference(ws, min_col=1, max_col=2, min_row=2, max_row=3)
chart.add_data(data)

# Add the chart to the worksheet
ws.add_chart(chart, "E2")

wb.save("project1.xlsx")






