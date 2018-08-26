'''
Validate three types of bracket '(', ')'
'[',']' and '{','}' in a given input string.
Strings can be empty with just brackets'''

def validate_brackets(string):
	stack = []
	for x in [c for c in string]:
		if x in ['{', '(', '[']:
			stack.append(x)
		elif x in [']', ')', '}']:
			if x == '}' and '{' == stack[-1]:
				stack.pop()
			elif x == ']' and '[' == stack[-1]:
				stack.pop()
			elif x == ')' and '(' == stack[-1]:
				stack.pop()
			else:
				print('Brackets are invalid')
				break
	if len(stack) != 0:
		print('Bracket validation failed')
	else:
		print('Bracket validation successful completed')


def gather_input():
	try:
		string = input('Please enter an expression to validate: ')
	except ValueError:
		print('Looks like its not a valid string')
	else:
		return string

my_string = gather_input()
validate_brackets(my_string)