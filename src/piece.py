def empty():
	'''returns a piece to represent an empty tile'''
	return Piece()


class Piece:
	def __init__(self, contents=None):
		self.contents = contents
