'''
   	This file is part of Holochess.

    Holochess is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Holochess is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Holochess.  If not, see <http://www.gnu.org/licenses/>.
'''
import piece


class Holoboard:
	def __init__(self, gametype=None, numorbits=2, orbitsize=12):
		sef.numorbits = numorbits
		self.orbitsize = orbitsize
		self.orbits = [CenterTile()]
		for i in range(orbits):
			if i == 0:
				self.orbits.append(Orbit(self.center, orbitsize))
			else:
				self.orbits.append(Orbit(self.orbits[i-1], orbitsize))

	def set_tile_contents(self, orbit, tileid=None, contents=piece.mpty()): #todo(aaron) improve param naming convention. orbitid and tileid or orbit and tile? why did I mix
	'''
	removes a piece at the specified tile from the board
	preconditions:
		orbit is an integer between 0 and 2 inclusive
			smaller numbers are closer to the hub, higher are closer to rim
			0 is the hub tile, 1 is inner orbit, 2 is outer orbit
			@todo(aaron) make dynamically sized boards
		tileid is always present if orbit is greather than 0
			@todo(aaron) write documentation on what tileid is for
	'''
		if not isinstance(contents, piece.Piece):
			raise InvalidTileContents("Cannot set type {} as tile contents.".format(type(contents)))
		if orbit == 0:
			if tileid != None:
				raise InvalidTileid("Cannot ")
			self.orbits[0] = contents
			#todo(aaron) decide if it should throw an exception when tileid isn't None but orbit is 0
		elif orbit in [i for i in range(1,self.numorbits)]:
			if tileid == None:
				raise InvalidTileid("{} is not a valid tileid".format(tileid))
			elif tileid >= orbits[orbit]:
				raise InvalidOrbitValue("Orbit value is {}, which it should not be.")
		else:
			self.orbits[orbit].tiles[tileid] = contents
			#@todo(aaron) refactor code so that...
			'''
			CenterTile is replaced by an orbit with size 1
			orbits can dynamically link to other orbits of different sizes 
			spend a bunch of time drawing on dry erase whiteboards making this work
			'''


class Tile: #probably doing abstract classes in python wrong
	def __init__(self contents=piece.empty()):
		self.contents = conents	
	if not isinstance(contents,piece.Piece:
			raise InvalidTileContents("Tile has contents of type {}. Should be Piece or None".format(type(contents)))

	@property
		def contents(self):
			return self._contents
		@contents.setter
		def contents(self, value):
			if not (isinstance(value, piece.Piece) or value == None):
				raise InvalidTileContents("Tried to set a tile's contents to type {}.".format(type(value)))
			self._contents = value


class OrbitTile(Tile):
	def __init__(self, contents=piece.empty(), rimnode=None, hubnode=None, twnode=None, wsnode=None):
		'''
		rimnode refers to the node that is 'rimwards' from this node, towards an outer orbit
		hubnode refers to the node that is 'hunwards' from this node, towards an inner orbit
		twnode refers to the node that is 'turnwise' (clockwise) from this node in the same orbit
		wsnode refers to the node that is 'widdershins' (counterclockwise) froom this node in the same orbit
		'''
		Tile.__init__(self, contents)
		#todo(aaron) make these into properties
		self.rimnode = rimnode
		self.hubnode = hubnode
		self.twnode = twnode
		self.wsnode = wsnode

	#todo(aaron) make the connectXX functions be nice properties and not do this weird java style encapsulation
	def connecttw(tile):
		self.twnode = tile
		tile.wsnode = self

	def connectws(tile):
		self.wsnode = tile
		tile.twnode = self

	def connectrim(tile):
		self.rimnode = tile
		tile.rimnode = self

	def connecthub(tile):
		self.hubnode = tile
		tile.hubnode = self


class CenterTile(Tile):
	def __init__(self, orbit=None, contents=piece.empty()):
		Tile.___init__(self,contents)
		if isinstance(orbit, Orbit):
			for tile in Orbit.tiles:
				tile.hubnode = self
		elif orbit != None: #this is bad logic @todo(aaron) condense the if and elif here into a single if
			raise OrbitIsntAnOrbit("You tried to construct a CenterTile with an orbit of type {}. You can only construct it with an orbit of type Orbit or None")
		else:
			self.orbit = orbit
		for tile in orbit.tiles:
			tile.hubnode = self


class Orbit: #todo(aaron): decide if it's a good idea to have an array of objects that act like a linkedlist
	def __init__(self, hub, rim=None, size=12):
		"""
		hub should always be a CenterTile or an Orbit
		rim should always be an Orbit or None
		default size is 12, this is to prevent magic numbers
		"""
		self.size = size
		self.hub = hub
		self.rim = rim
		self.tiles = [OrbitTile for i in range(size)]

		for i in range(size):
			self.tiles[i].connectws(tiles[i-1])

		if isinstance(rim, Orbit):
			if rim.size == self.size:
				for i in range(size):
					self.tiles[i].connectrim(rim.tiles[i])
				rim.hub = self
			else:
				raise UnmatchingOrbitSizes("You tried to construct an Orbit of size {} with a rim of size {}.".format(self.size,rim.size))
		elif rim == None:
			for tile in tiles:
				tile.rimnode = None
		else:
			raise OrbitRimInvalidType("You tried to construct an Orbit with a rim of type {}. It should only be type Orbit or type None.".format(type(rim)))

		if isinstance(hub, Orbit):
			if hub.size == self.size
				for i in range(size):
					self.tiles[i].connecthub(hub.tiles[i])
				hub.rom = self
			else:
				raise UnmatchingOrbitSizes("You tried to construct an Orbit of size {} with a hub orbit of size {}.".format(self.size,hub.size))
		elif isinstance(hub, CenterTile):
			for tile in tiles:
				tile.hubnode = hub
		else:
			raise OrbitHubInvalidType()
	#cool, it has a sexy init function, but what other things will it need?
	#time to put more code into Holoboard later on..

'''
@todo(aaron):
* Condense these, there's definitely many of these that can be condensed
* (maybe?) Add docsctrings explaining when these should be used
* (maybe?) Put these into their own file (seems like an awesome idea)
'''
class UnmatchingOrbitSizes(Exception):
	pass


class OrbitRimInvalidType(Exception):
	pass


class OrbitHubInvalidType(Exception):
	pass


class OrbitIsntAnOrbit(Exception): #this is the worst name of an exception type ever
	pass #seriously this is SO BAD


class InvalidTileContents(Exception):
	pass


class InvalidTileid(Exception):
	pass


class InvalidOrbitValue(Exception):
	pass