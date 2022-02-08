sales = dict()
custSales = dict()
record = list()
custList = list()

while True:
    input_line = input()

    if input_line == '':
        break

    record = input_line.split()
    sales.setdefault(record[0], {})
    custSales = sales.get(record[0])
    if record[1] not in custSales:
        custSales[record[1]] = int(record[2])
    else:
        count = custSales.get(record[1])
        custSales[record[1]] = count + int(record[2])

custList = sorted(list(sales))

for cust in custList:
    print(f"{cust}:")
    custItemList = list(sales[cust].items())
    custItemList.sort()
    for item in custItemList:
        print(item[0], item[1])
