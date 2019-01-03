import pygame
import src.Classes.Game as Game
import src.Utility.GameValues as GV


class Main():

	def __init__(self):

		self.running = True
		pygame.init()
		self.gameDisplay = pygame.display.set_mode(GV.Game.displaySize.value)
	    #game = Game.Game((12, 18))


	def draw(self):
		self.gameDisplay.blit(GV.Images.backgroundImage.value, (0,0))


	def handleEvents(self):
		pass

	def runGame(self):
		
		clock = pygame.time.Clock()

		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

	
			self.draw()

			self.handleEvents()
	

			pygame.display.update()
			clock.tick(24)


		pygame.quit()

if __name__ == '__main__':
	prog = Main()
	prog.runGame()