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

gameDisplay = pagame.display.set_mode(widow_size)
pagame.display.set_caption("Space Invaders")

game_clock = pygame.time.Clock()
################################################################

################################################################
# Define Colors
################################################################
black = 0, 0, 0
white = 255, 255, 255
################################################################

################################################################
# Import Images
# xxx = pygame.image.load("images/img.png")
################################################################
startScreenBackground = None
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
			pass


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