import re

def problem_1():
	return re.compile('a')

def problem_2():
	return re.compile(r'[a-zA-Z]*a[a-zA-z]*')

def problem_3():
	return re.compile(r'[0-9]+')

def problem_4():
	return re.compile(r'[Hh]ello[o]*')

def problem_5():
	return re.compile(r'\b[Hh]ello[o]*\b')