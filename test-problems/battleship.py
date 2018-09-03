'''Given an integer N, create a grid of size N x N and find a battleship
3 spaces long within in. the ship can be placed randomly either vertical
or horizontal. Handle the creation of the grid, placement of the ship
and find the ship using the bomb_location function and return the 
co ordinates'''

class board:

	def __init__(self, size=None):
		self.size = size
		self.gameboard = None

	def create_board(self):
		if self.size is None:
			while True:
				try:
					self.size = int(input('Enter the size of the game board:\t'))
				except ValueError:
					print('Please enter a valid integer')
					continue
				break

		self.gameboard = list(range(0,self.size))
		print(self.gameboard)


# The driver code
bs = board(5)
bs.create_board()

