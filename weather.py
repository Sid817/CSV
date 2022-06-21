with open("weather_data.csv") as file:
    data=file.readlines()
    print(data)




import csv

with open("weather_data.csv") as data:
    data=csv.reader(data)
    temperatures = []
    i=0
    for row in data:
        # print(row)
        #This aligns much more with the row-column(tabular) format, so becomes easier to work with
        if i!=0:
            temperatures.append(int(row[1]))
        i+=1

    print(temperatures)



import pandas

data=pandas.read_csv("weather_data.csv")
print(type(data))

