# TestRobotFunctions.py

# import statements
import unittest
import ParserFunctions

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


# Run the tests

if __name__ == '__main__':
	unittest.main()