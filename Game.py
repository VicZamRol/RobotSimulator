# Game.py

# This file includes the code to read the inputs from standart and external file,
# also includes the function which categorises the commands and execute them.

# import statements
import sys
import RobotFunctions
import ParserFunctions

# Function to read inputs

def game():

	commands = sys.stdin.read()		# Read commands from standart input
	command_list = commands.strip().split('\n')
	run_game(command_list)

# Function to categorise input commands and execute them

def run_game(command_list):

	robot = None
	result = None

	for c in command_list:
		if ParserFunctions.isValidCommand(c):		# Checks if the command is valid
			command_name = c.split(' ')[0]

			if command_name == 'PLACE':
				arg_x, arg_y, orientation = ParserFunctions.argumentExtractionPlace(c)	# Extraction of PLACE arguments

				if ParserFunctions.isInRange(arg_x, arg_y):
					robot = RobotFunctions.Robot(arg_x, arg_y, orientation)		# Places the robot

			elif command_name == 'MOVE' and robot != None:
				robot.move()
			elif command_name == 'RIGHT' and robot != None:
				robot.right()
			elif command_name == 'LEFT' and robot != None:
				robot.left()
			elif command_name == 'REPORT' and robot != None:
				result = robot.report()
	return result


# Run the game

if __name__ == '__main__':
	game()
