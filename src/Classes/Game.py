from src.Interfaces.IGame import IGame
import src.Utility.GameValues as GV
import src.Utility.Errors as err


class Game(IGame):

	def __init__(self):
		print("Created a game Object!")

	def dummy(self):
		print("Now we have dummy method")
		raise NotImplementedError