from enum import Enum
import pygame

class Game(Enum):
	cell_height = 32
	cell_width  = 32
	displaySize = (cell_width * 32, cell_height * 16)

class Images(Enum):
	backgroundImage = pygame.image.load("res/backgroundImage.jpg")