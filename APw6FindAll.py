import re

regexp = r'<i>(.*?)</i>'
answer = list()

while True:
    input_str = input()
    if input_str == '':
        break
    else:
        result = re.findall(regexp, input_str)
        answer.append(result)

for item in answer:
    if len(item) != 0:
        print(*item, sep='\n')
