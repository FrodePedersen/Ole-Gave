from src.Interfaces.IGame import IGame
import src.Utility.GameValues as GV
import src.Utility.Errors as err


class Game(IGame):

	def __init__(self, n_cells):
		(n_rows, n_cols) = n_cells #Number of cells in the game
		height, width = n_rows * GV.Game.cell_height.value, n_cols * GV.Game.cell_height.value
		print("Created a game Object!")
		print("rows:" + str(n_rows))
		print(f"rows: {n_rows}, cols: {n_cols}, height: {height}, width: {width}")

	def dummy(self):
		print("Now we have dummy method")
		raise NotImplementedError