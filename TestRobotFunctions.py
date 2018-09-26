# TestRobotFunctions.py

# import statements
import unittest
import ParserFunctions
import RobotFunctions
import Game

class TestSystemFunctions(unittest.TestCase):

	# Test Parser Functions

	def test_isValidCommand_forMOVE(self):
		result = ParserFunctions.isValidCommand("MOVE")
		self.assertEqual("valid command", result)

	def test_isValidCommand_forLEFT(self):
		result = ParserFunctions.isValidCommand("LEFT")
		self.assertEqual("valid command", result)

	def test_isValidCommand_forRIGHT(self):
		result = ParserFunctions.isValidCommand("RIGHT")
		self.assertEqual("valid command", result)

	def test_isValidCommand_forREPORT(self):
		result = ParserFunctions.isValidCommand("REPORT")
		self.assertEqual("valid command", result)

	def test_isValidCommand_forPLACE(self):
		result = ParserFunctions.isValidCommand("PLACE 0,1,NORTH")
		self.assertEqual("valid command", result)

	def test_isValidCommand_forNoValidCommand(self):
		result = ParserFunctions.isValidCommand("HELLO")
		self.assertEqual("invalid command", result)

	def test_isValidCommand_forNoValidPLACEOrientation(self):
		result = ParserFunctions.isValidCommand("PLACE 0,1,NORT")
		self.assertEqual("invalid command", result)

	def test_isValidCommand_forNoValidPLACEPosition(self):
		result = ParserFunctions.isValidCommand("PLACE 4,5,NORTH")
		self.assertEqual("invalid command", result)

	# Test Robot Functions

	def test_Robot_PlaceRobotInBoard(self):
		new_robot = RobotFunctions.Robot(0, 1, 'NORTH')
		self.assertEqual(0, new_robot.getX())
		self.assertEqual(1, new_robot.getY())
		self.assertEqual('NORTH', new_robot.getFacing())

	def test_Rotate_fromNorthToRight(self):
		robot = RobotFunctions.Robot(0, 1, 'NORTH')
		robot.right()	# Right rotation
		result = robot.getFacing()
		self.assertEqual('EAST', result)

	def test_Rotate_fromSouthToRight(self):
		robot = RobotFunctions.Robot(0, 1, 'SOUTH')
		robot.right()	# Right rotation
		result = robot.getFacing()
		self.assertEqual('WEST', result)

	def test_Rotate_fromEastToRight(self):
		robot = RobotFunctions.Robot(0, 1, 'EAST')
		robot.right()	# Right rotation
		result = robot.getFacing()
		self.assertEqual('SOUTH', result)

	def test_Rotate_fromWestToRight(self):
		robot = RobotFunctions.Robot(0, 1, 'WEST')
		robot.right()	# Right rotation
		result = robot.getFacing()
		self.assertEqual('NORTH',result)

	def test_Rotate_fromNorthToLeft(self):
		robot = RobotFunctions.Robot(0, 1, 'NORTH')
		robot.left()	# Left rotation
		result = robot.getFacing()
		self.assertEqual('WEST', result)

	def test_Rotate_fromSouthToLeft(self):
		robot = RobotFunctions.Robot(0, 1, 'SOUTH')
		robot.left()	# Left rotation
		result = robot.getFacing()
		self.assertEqual('EAST', result)

	def test_Rotate_fromEastToLeft(self):
		robot = RobotFunctions.Robot(0, 1, 'EAST')
		robot.left()	# Left rotation
		result = robot.getFacing()
		self.assertEqual('NORTH', result)

	def test_Rotate_fromWestToLeft(self):
		robot = RobotFunctions.Robot(0, 1, 'WEST')
		robot.left()	# Left rotation
		result = robot.getFacing()
		self.assertEqual('SOUTH', result)

	def test_Move_facingNorth(self):
		robot = RobotFunctions.Robot(0, 1, 'NORTH')
		robot.move()	# Move robot
		self.assertEqual(0, robot.getX())
		self.assertEqual(2, robot.getY())
		self.assertEqual('NORTH',robot.getFacing())

	def test_Move_facingSouth(self):
		robot = RobotFunctions.Robot(0, 1, 'SOUTH')
		robot.move()	# Move robot
		self.assertEqual(0, robot.getX())
		self.assertEqual(0, robot.getY())
		self.assertEqual('SOUTH', robot.getFacing())

	def test_Move_facingEast(self):
		robot = RobotFunctions.Robot(0, 1, 'EAST')
		robot.move()	# Move robot
		self.assertEqual(1, robot.getX())
		self.assertEqual(1, robot.getY())
		self.assertEqual('EAST', robot.getFacing())

	def test_Move_facingWest(self):
		robot = RobotFunctions.Robot(1, 1, 'WEST')
		robot.move()	# Move robot
		self.assertEqual(0, robot.getX())
		self.assertEqual(1, robot.getY())
		self.assertEqual('WEST', robot.getFacing())

	def test_Move_forNorthBoundariesfacingNorth(self):
		robot = RobotFunctions.Robot(1, 4, 'NORTH')
		robot.move()	# Move robot
		self.assertEqual(1, robot.getX())
		self.assertEqual(4, robot.getY())
		self.assertEqual('NORTH', robot.getFacing())

	def test_Move_forSouthBoundariesfacingSouth(self):
		robot = RobotFunctions.Robot(1, 0, 'SOUTH')
		robot.move()	# Move robot
		self.assertEqual(1, robot.getX())
		self.assertEqual(0, robot.getY())
		self.assertEqual('SOUTH', robot.getFacing())

	def test_Move_forEastBoundariesfacingEast(self):
		robot = RobotFunctions.Robot(4, 1, 'EAST')
		robot.move()	# Move robot
		self.assertEqual(4, robot.getX())
		self.assertEqual(1, robot.getY())
		self.assertEqual('EAST', robot.getFacing())

	def test_Move_forWestBoundariesfacingWest(self):
		robot = RobotFunctions.Robot(0, 1, 'WEST')
		robot.move()	# Move robot
		self.assertEqual(0, robot.getX())
		self.assertEqual(1, robot.getY())
		self.assertEqual('WEST', robot.getFacing())

	def test_Report(self):
		robot = RobotFunctions.Robot(0, 1, 'WEST')
		result = robot.report()
		self.assertEqual('0,1,WEST', result)

	# Test Game Functions

	def test_Game_forValidSequence_1(self):
		sequenceCommands = ['PLACE 0,0,NORTH', 'MOVE', 'REPORT']
		result = Game.run_game(sequenceCommands)
		self.assertEqual('0,1,NORTH', result)

	def test_Game_forValidSequence_2(self):
		sequenceCommands = ['PLACE 0,0,NORTH', 'LEFT', 'REPORT']
		result = Game.run_game(sequenceCommands)
		self.assertEqual('0,0,WEST', result)

	def test_Game_forValidSequence_3(self):
		sequenceCommands = ['PLACE 1,2,EAST', 'MOVE', 'MOVE', 'LEFT', 'MOVE', 'REPORT']
		result = Game.run_game(sequenceCommands)
		self.assertEqual('3,3,NORTH', result)

	def test_Game_forInvalidSequence_1(self):
		sequenceCommands = ['PLACE 9,2,EAST', 'MOVE', 'MOVE', 'LEFT', 'PLACE 1,2,EAST', 'MOVE', 'MOVE', 'LEFT', 'MOVE', 'REPORT']
		result = Game.run_game(sequenceCommands)
		self.assertEqual('3,3,NORTH', result)

	def test_Game_forInvalidSequence_2(self):
		sequenceCommands = ['MOVE', 'MOVE', 'LEFT', 'PLACE 1,2,EAST', 'MOVE', 'PLACE 9,2,EAST', 'MOVE', 'LEFT', 'MOVE', 'REPORT']
		result = Game.run_game(sequenceCommands)
		self.assertEqual('3,3,NORTH', result)


# Run the tests

if __name__ == '__main__':
	unittest.main()