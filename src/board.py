import piece
class HoloChessBoard:
	def __init__(self, gametype=None):
		#setup the tiles in their orbits
		pass

	def remove_piece(self, tile):
	'''removes a piece at the specified tile from the board'''
		pass

class Tile:
	def __init__(self, contents=piece.empty()):
		self.contents = conents

class OrbitTile(Tile):
	def __init__(self, contents=piece.empty(), rimnode=None, hubnode=None, twnode=None, wsnode=None):
		'''
		rimnode refers to the node that is 'rimwards' from this node, towards an outer orbit
		hubnode refers to the node that is 'hunwards' from this node
		'''
		Tile.__init__(self,contents=piece.empty())
		self.rimnode = rimnode
		self.hubnode = hubnode
		self.nodecleanup()

	def nodecleanup():
		if rimnode != None:
			rimnode.hubnode = self
		if hubnode != None and not isinstance(hubnode,CenterTile):
			hubnode.rimnode = self


class CenterTile(Tile):
	def __init__(self, contents=piece.empty(), exits=[None for i in range(6)]):
		Tile.init(self,contents)
		self.exits = exits
		self.nodecleanup


	def nodecleanup():
		for exit in exits:
			if exit != None:
				exit.hubnode = self