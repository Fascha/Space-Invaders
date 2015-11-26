#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################
# Imports
################################################################
import sys
sys.path.append("modules") #For PyGame
import pygame
from pygame.locals import *
################################################################

################################################################
# Initialize PyGame, Framerate and Game Window
################################################################
pygame.init()

window_width = 800
window_height = 600
window_size = window_width, window_height

gameDisplay = pygame.display.set_mode(window_size)
pygame.display.set_caption("Space Invaders")

game_clock = pygame.time.Clock()
game_clock.tick(60)
################################################################

################################################################
# Define Colors
################################################################
black = 0, 0, 0
white = 255, 255, 255
################################################################

################################################################
# Import Images
# xxx = pygame.image.load("data/images/img.png")
################################################################
startScreenBackground = pygame.image.load("data/images/startScreen.png")
gameBackground = None
gameOverScreenBackground = None
################################################################



class SpaceInvaders:

	class Player:
		pass
	
	class Alien:
		pass
	
	class Brick:
		pass
	
	class Mothership:
		pass

	class Bullet:
		pass


	def drawAliens():
		pass
	
	def drawPlayer():
		pass
	
	def drawAlienBullets():
		pass
	
	def drawPlayerBullet():
		pass

	def drawMothership():
		pass

	def drawBricks():
		pass
	
	################################################################
	# Setup a new Game
	################################################################
	def setupNewGame():
		pass


	################################################################
	# Game Loop
	################################################################
	def gameLoop():
		while true:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					break


	################################################################
	# Start Screen
	################################################################	
	def startScreen():
		while true:
			gameDisplay.blit(startScreenImage,(0,0))
			pygame.display.update()


	################################################################
	# Game Over Screen
	################################################################
	def gameOverScreen():
		while true:
			pass


	def run():
		startScreen()



################################################################
# Hier wird das Spiel ausgefuehrt
################################################################
SpaceInvaders.run()