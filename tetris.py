import pygame
from pygame.locals import *

pygame.init()
max_x = 640
max_y = 480
block_size = 20
screen = pygame.display.set_mode((max_x, max_y))

cell = pygame.Surface((19, 19))
cell.fill((0,0,0))

matrix = pygame.Surface((block_size*10+11,block_size*20+22))
matrix.fill((255,255,255))
matrix_pos = ((max_x-(block_size*10+11))/2,15)

for i in range(10):
	for j in range(20):
		matrix.blit(cell, (i*block_size+i+1,j*block_size+j+2))

pygame.display.set_caption('Tetris')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				quit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.quit()
			quit()

	screen.fill((0,0,0))
	screen.blit(matrix, matrix_pos)

	# pygame.draw.rect(screen,(50,50,50),[300,2,100,40])

	pygame.display.update()