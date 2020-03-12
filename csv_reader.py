# import pandas
from resources import unique, get_tags, read_csv
# data = pandas.read_csv("Data.csv", ",")

# un = get_tags(data)
# print(len(un))

tags, data = read_csv("Data.csv")
print(tags)
print(data)
