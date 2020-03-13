def findProducts(data):
    customers = list()
    for i in range(len(data)):
        if data[i][3] not in customers:
            customers[data[i][3]].data[i][4]
        else:
            customers[data[i][3]].append({data[i][4]})

    for i in customers:
        print(i)
        for j in i:
            print(j)