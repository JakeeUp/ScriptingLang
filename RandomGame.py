

import pygame 
import random 
  
# Initialize the pygame 
pygame.init() 
  
# create the screen 
screen = pygame.display.set_mode((800, 600)) 
  
# Background 
background = pygame.image.load('background.jpg') 
  
# Title and Icon 
pygame.display.set_caption("Jumping Game") 

 # Player 
playerImg = pygame.image.load('player.png') 
playerX = 370
playerY = 480

 # Enemy 

enemyImg = [] 

enemyX = [] 

enemyY = []

num_of_enemies = 6

for i in range(num_of_enemies):     

     enemyImg.append(pygame.image.load('enemy.png'))     

     enemyX.append(random.randint(0,735))     

     enemyY.append(random.randint(50,150))    # Game Loop    running = True    while running:        # RGB - Red, Green, Blue        screen.fill((0, 0, 0))        # Background Image        screen.blit(background, (0, 0))        for i in range(num_of_enemies):         