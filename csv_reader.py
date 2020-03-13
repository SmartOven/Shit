<<<<<<< Updated upstream
from resources import unique, read_csv, get_check, print_check

tags, data = read_csv("Data.csv")
check = get_check(tags, data)
print_check(check)
=======
# import pandas
from resources import unique, read_csv
from show_users_products import *
# data = pandas.read_csv("Data.csv", ",")

# un = get_tags(data)
# print(len(un))

tags, data = read_csv("Data.csv")
# print(tags)
# printData(data)
findProducts(data)

>>>>>>> Stashed changes
