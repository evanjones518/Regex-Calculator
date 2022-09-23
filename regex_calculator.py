#!C:/Users/evanj/AppData/Local/Programs/Python/Python310/python.exe
import re
"""This calculator takes a mathematical expression from keyboard input and calculates it based on the order of operations."""

'''This function takes a match from the regex patterns and operates on them, returning the evaluated chunk.'''
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

'''Takes the input expression and all occurances of an operation type'''
def replace_element(input_expression, all_occurances):
	for occurance in all_occurances:
		evaluated = calculate(occurance)
		input_expression = input_expression.replace(occurance, str(evaluated))
	return input_expression

'''Regex patterns for matching purposes.'''
parentheses_pattern = r'(\([\-0-9\.]+ [\+\-\*\/] [\-0-9\.]+\))'
division_pattern = r'([\-0-9\.]+ \/ [\-0-9\.]+)'
multiply_pattern = r'([\-0-9\.]+ \* [\-0-9\.]+)'
addition_pattern = r'([\-0-9\.]+ \+ [\-0-9\.]+)'
subtraction_pattern = r'([\-0-9\.]+ \- [\-0-9\.]+)'
has_parentheses = r'[\(\)]'
completed_pattern = r'([\-0-9\.])'

print("Welcome to the new and improved Regex Calculator! Valid entries include spaces between every element. Example:\n5 + 9 - (4 * 2)")
continue_calc = True
while continue_calc == True:
	
	
	expression = input("Enter an expression:\n>>>")
	if expression.isalpha():
		print("Invalid input!")
		continue

	while True:
		if re.search(parentheses_pattern, expression):
			occurances = re.findall(parentheses_pattern, expression)
			print(occurances)
			expression = replace_element(expression, occurances)
			print(expression)
		else:
			break

	while True:
		if re.search(division_pattern, expression):
			occurances = re.findall(division_pattern, expression)
			print(occurances)
			expression = replace_element(expression, occurances)
			print(expression)
		else:
			break

	while True:
		if re.search(multiply_pattern, expression):
			occurances = re.findall(multiply_pattern, expression)
			print(occurances)
			expression = replace_element(expression, occurances)
			print(expression)
		else:
			break

	while True:
		if re.search(subtraction_pattern, expression):
			occurances = re.findall(subtraction_pattern, expression)
			print(occurances)
			expression = replace_element(expression, occurances)
			print(expression)
		else:
			break

	while True:
		if re.search(addition_pattern, expression):
			occurances = re.findall(addition_pattern, expression)
			print(occurances)
			expression = replace_element(expression, occurances)
			print(expression)
		else:
			break

	while True:
		continue_program = input("Would you like to perform another calculation?\n(yes/no)\n>>> ")
		if continue_program.lower() == 'yes':
			break
		elif continue_program.lower() == 'no':
			exit()
		else:
			print("Invalid input!")