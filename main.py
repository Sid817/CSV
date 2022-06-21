# # with open("weather_data.csv") as file:
# #     data=file.readlines()
# #     print(data)
#
#
#
# #
# # import csv
# #
# # with open("weather_data.csv") as data:
# #     data=csv.reader(data)
# #     temperatures = []
# #     i=0
# #     for row in data:
# #         # print(row)
# #         #This aligns much more with the row-column(tabular) format, so becomes easier to work with
# #         if i!=0:
# #             temperatures.append(int(row[1]))
# #         i+=1
# #
# #     print(temperatures)
#
#
#
# import pandas
#
# data=pandas.read_csv("weather_data.csv")
# print(type(data))
#
#
#
#
# #the first challlenge can be done in a single line of code in pandas
# #the syntax to print all the items of a column is as follows
# #data[column_name]. Python automatically identifies the column and pri



#the great squirrel data analysis in python

import pandas

squirrel_data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors=squirrel_data["Primary Fur Color"]
data_dict=colors.to_dict()
print(data_dict)

color_list=["gray","cinnamon","black"]
count_gray=0
count_cinnamon=0
count_black=0
for key,value in data_dict.items():
    print(value)

    if value=="Gray":
        count_gray+=1
    elif value=="Cinnamon":
        count_cinnamon+=1
    elif value=="Black":
        count_black+=1


count_list=[count_gray,count_cinnamon,count_black]

color_dict={"Fur Color":color_list, "Count":count_list}
# print(color_dict)
color_data=pandas.DataFrame(color_dict)
color_data.to_csv("color_data.csv")
