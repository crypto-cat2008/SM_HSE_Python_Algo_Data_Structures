import json

data = list()

input_files = input().split()
output_file = input()

for file in input_files:
    with open(file, 'r')as file1:
        for line in file1:
            x = json.loads(line)
            data.append(x)


data.sort(key=lambda x1: (x1["date"], x1["consumer_id"]))

with open(output_file, 'w') as file3:
    for item in data:
        data_line = item["date"] + '\t' + item["message"] + '\n'
        file3.write(data_line)
