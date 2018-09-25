# Robot Functions

# import statements
import ParserFunctions

class Robot:

	def __init__(self, x, y, orientation):

		self.x = x
		self.y = y
		self.orientation = orientation

	def getX(self):

		return self.x

	def getY(self):

		return self.y

	def getFacing(self):

		return self.orientation

	def right(self):

		if self.orientation == 'NORTH':
			self.orientation = 'EAST'
		elif self.orientation == 'SOUTH':
			self.orientation = 'WEST'
		elif self.orientation == 'EAST':
			self.orientation = 'SOUTH'
		else:
			self.orientation = 'NORTH' 

	def left(self):

		if self.orientation == 'NORTH':
			self.orientation = 'WEST'
		elif self.orientation == 'SOUTH':
			self.orientation = 'EAST'
		elif self.orientation == 'EAST':
			self.orientation = 'NORTH'
		else:
			self.orientation = 'SOUTH'

	def move(self):

		if self.orientation == 'NORTH':
			new_position = int(self.y) + 1
			if ParserFunctions.isInRange(self.x, new_position):
				self.y = new_position
		elif self.orientation == 'SOUTH':
			new_position = int(self.y) - 1
			if ParserFunctions.isInRange(self.x, new_position):
				self.y = new_position
		elif self.orientation == 'EAST':
			new_position = int(self.x) + 1
			if ParserFunctions.isInRange(new_position, self.y):
				self.x = new_position
		elif self.orientation == 'WEST':
			new_position = int(self.x) - 1
			if ParserFunctions.isInRange(new_position, self.y):
				self.x = new_position

	def report(self):
		result = str(self.x) + ',' + str(self.y) + ',' + str(self.orientation)
		print(result)
		return result