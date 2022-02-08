import json
line = []
answer = []


def read_json(json_str):
    global line
    if len(json_str) == 0:
        answer.append(line)
    for key, value in json_str.items():
        line.append(key)
        if isinstance(value, dict):
            read_json(value)
    line = line[:-1]


fileName = input()

with open(fileName) as f:
    log = json.load(f)
    read_json(log)
    for item in sorted(answer):
        print(*item, sep='/')
