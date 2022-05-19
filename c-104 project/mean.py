import csv
import plotly.express as px
import pandas as pd


with open('SOCR-HeightWeight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)

total_height=0
total_entries=len(file_data)

data = []
for i in file_data:
    total_height=total_height+float(i[1])

mean = total_height/total_entries

print(str(mean))