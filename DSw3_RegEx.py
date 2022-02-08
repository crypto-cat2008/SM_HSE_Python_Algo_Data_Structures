import re

def problem_1():
	return re.compile(r'-?[0-9]+')

def problem_2():
	return re.compile(r'\b[0-9]+[.]?[0-9]*')

def problem_3():
	return re.compile(r'\b[0-1]?[0-9]:[0-5][0-9]|\b[2][0-3]:[0-5][0-9]')

def problem_4():
	return re.compile(r'\b\d\d\d\d-[0]\d-[0-2]\d|\b\d\d\d\d-[1][0-2]-[0-2]\d|\b\d\d\d\d-[0]\d-[3][0-1]|\b\d\d\d\d-[1][0-2]-[3][0-1]')

def problem_5():
	return re.compile(r'\b[a-zA-Z0-9-_][a-zA-Z0-9-_][a-zA-Z0-9-_][a-zA-Z0-9-_]*')

def problem_6():
	return re.compile(r'\b[a-zA-Z0-9-_.]+@[a-zA-Z]+(?:\.[a-zA-Z]+)+')

def problem_7():
	return re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b')

def problem_8():
	return re.compile(r'\b(?:http://|https://){1}[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?:[/]*[a-zA-Z0-9.-_]*)')