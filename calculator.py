#!C:/Users/evanj/AppData/Local/Programs/Python/Python310/python.exe
import re
import math
"""The idea here is to take input and use regexes to put the operations in a workable order according to pemdas."""

def calculate(expression_slice):
	result = 0
	expression_slice = re.sub(has_parentheses, '', expression_slice)
	expression_slice = expression_slice.split()

	if "+" in expression_slice:
		result = float(expression_slice[0]) + float(expression_slice[2])
		return result

	if "-" in expression_slice:
		result = float(expression_slice[0]) - float(expression_slice[2])
		return result

	if "*" in expression_slice:
		result = float(expression_slice[0]) * float(expression_slice[2])
		return result

	if "/" in expression_slice:
		result = float(expression_slice[0]) / float(expression_slice[2])
		return result

def replace_element(input_expression, all_occurances):
	for occurance in all_occurances:
		evaluated = calculate(occurance)
		input_expression = input_expression.replace(occurance, str(evaluated))
	return print(input_expression)



parentheses_pattern = r'(\(\d+ [\+\-\*\/] \d+\))'
division_pattern = r'(\d+ \/ \d+)'
multiply_pattern = r'(\d+ \* \d+)'
addition_pattern = r'(\d+ \+ \d+)'
subtraction_pattern = r'(\d+ \- \d+)'
has_parentheses = r'[\(\)]'

print("Welcome to this Regex Calculator!")

expression = input("Enter an expression:\n>>>")

occurances = re.findall(parentheses_pattern, expression)
indices = re.search(parentheses_pattern, expression)

#expression = expression.replace(str(occurances[0]), str(result))

#print(expression)

replace_element(expression, occurances)
