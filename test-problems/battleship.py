'''Given an integer N, create a grid of size NxN and find a battleship
3 spaces long within NxN. the ship can be placed randomly either vertical
or horizontal. Handle the creation of the grid, placement of the ship
and find the ship using the bomb_location function and return the
co ordinates'''
import random

class board:

	def __init__(self, size=None):
		self.size = size
		self.gameboard = []
		self.ship = []

	def create_board(self):
		if self.size is None:
			while True:
				try:
					self.size = int(input('Enter the size of the game board: '))
					if self.size < 3:
						raise ValueError
				except ValueError:
					print('Please enter a valid size, must be an integer above 3')
					continue
				break

		for x in range(0, self.size):
			self.gameboard.append(list(range(0,self.size)))
		#print(self.gameboard)

	def place_ship(self):
		x = random.randint(0,1) # Defines whether the ship is horizontal (0) or vertical (1)
		y = [random.randint(0, self.size), random.randint(0, self.size)] # starting co ordinate of the ship
		for z in range(0,3):
			if x == 0:
				temp = (y[0] + z, y[1])
			else:
				temp = (y[0], y[1] + z)
			self.ship.append(temp)
		#print(self.ship)

	def bomb_location(self):
		found = 0
		for a in range(0, self.size):
			for x in range(a, self.size, 2):
				print(a, x)
				if (a, x) in set(self.ship):
					found = 1
					break
			if found == 1:
				break

		if found == 1:
			if ((a + 1, x) in set(self.ship)) or ((a - 1, x) in set(self.ship)):
				print('Found the ship!')
				print('ship is vertical')
			else:
				print('Found the ship!')
				print('ship is horizontal')
			print(self.ship)
			print(a, x)

# The driver code
game = board()
game.create_board()
game.place_ship()
game.bomb_location()
