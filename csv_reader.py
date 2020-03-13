from resources import unique, read_csv, get_check, print_check

tags, data = read_csv("Data.csv")
# print(tags)
# print(data)
# for d in data:
#     print(d)
check = get_check(tags, data)
print_check(check)
