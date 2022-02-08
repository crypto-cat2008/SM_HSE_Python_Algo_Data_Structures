import re


#pattern = re.compile(r'\b(?:http://|https://){1}[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+[/]*')
pattern = re.compile(r'\b(?:http://|https://){1}[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?:[/]*[a-zA-Z0-9.-_]*)')
text = "Welcome to https://wel.com/e, stranger!"
#text = '2. bb -3.3b cc'
#text = "His level of English profficiency is B2"

print(re.findall(pattern, text))

p = re.compile(r"(?:[0-1]?[0-9]|2[0-3]):[0-5][0-9]")
print(re.findall(p, 'At 17:00, or at 14:00, or at 25:61'))