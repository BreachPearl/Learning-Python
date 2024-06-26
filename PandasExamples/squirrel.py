import pandas as pd

data=pd.read_csv('PandasExamples/Squirrel_Data.csv')

distinct_values=data["Primary Fur Color"].unique()
print(distinct_values)
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

squirrel_dict={
    'Furcolor':['gray','cinnamon','black'],
    'count':[grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}
fur_data=pd.DataFrame(squirrel_dict)
fur_data.to_csv("C:/Learning Python/PandasExamples/furdata.csv")