# ParserFunctions.py

# Functions to check the commands

def isValidCommand(command):

	if command == 'MOVE' or command == 'LEFT' \
	   	or command == 'RIGHT' or command == 'REPORT':
		result = 'valid command'
	elif command.split(' ')[0] == 'PLACE':
		result = isValidPLACECommand(command)
	else:
		result = 'invalid command'
	return result

def isValidPLACECommand(command):

	args_string = command.split(' ')[1]
	arg_array = args_string.split(',')
	result = 'invalid command'

	if len(arg_array) == 3:
	 	if isInRange(arg_array[0],arg_array[1]) :
	 		if isValidOrientation(arg_array[2]):
	 			result = 'valid command'

	return result

def isInRange(x, y):

	result = False

	if int(x) in range(5) and int(y) in range(5):
		result = True

	return result

def isValidOrientation(orientation):

	result = False

	if orientation == 'NORTH' or orientation == 'SOUTH' \
	   	or orientation == 'WEST' or orientation == 'EAST':
		result = True

	return result