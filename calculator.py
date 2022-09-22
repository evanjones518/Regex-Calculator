#!C:/Users/evanj/AppData/Local/Programs/Python/Python310/python.exe
import re
import math
"""The idea here is to take input and use regexes to put the operations in a workable order according to pemdas."""

def calculate(expression_slice):
	if "+" in expression_slice:
		pass
	if "-" in expression_slice:
		pass
	if "*" in expression_slice:
		pass
	if "/" in expression_slice:
		pass

parentheses_pattern = r'(\(\d+ [\+\-\*\/] \d+\))'
division_pattern = r'(\d+ \/ \d+)'
multiply_pattern = r'(\d+ \* \d+)'
addition_pattern = r'(\d+ \+ \d+)'
subtraction_pattern = r'(\d+ \- \d+)'

print("Welcome to this Regex Calculator!")


expression = input("Input an expression to be evaluated: \n>>> ")


match = re.findall(parentheses_pattern, expression)

print(match)
