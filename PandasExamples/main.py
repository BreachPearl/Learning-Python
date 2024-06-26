# with open("PandasExamples/weather_data.csv") as file:
#     data=file.readlines()
# strip_data=[]
# for x in data:
#     stripped_data=x.strip("\n")
#     strip_data.append(stripped_data)
# print(strip_data)

# import csv

# with open("PandasExamples/weather_data.csv") as file:
#     data=csv.reader(file)
#     temp=[]
#     for row in data:
#         if row[1]!="temp":
#             temp.append(int(row[1]))
#     print(temp)

import pandas as pd

data=pd.read_csv('PandasExamples/weather_data.csv')

print(data[data.temp==data.temp.max()])
