from _pytest.nodes import Item

from my_functions import *
from my_constants import *
from classes.tetrimino import Tetrimino
import pygame
from pygame.locals import *
from copy import deepcopy

pygame.init()

screen = pygame.display.set_mode((MAX_X, MAX_Y))

matrix = pygame.Surface((BLOCK_SIZE*10+11, BLOCK_SIZE*20+22))
matrix.fill((255, 255, 255))
matrix_pos = ((MAX_X-(BLOCK_SIZE*10+11))/2, 15)

# cria cada item cell
cell = []
for i in range(10):
	cell.append([])
	for j in range(20):
		cell[i].append([])
		cell[i][j] = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
		cell[i][j].fill((0, 0, 0))

pygame.display.set_caption('Tetris')

mino = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
ghost_mino = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
ghost_mino.fill((120, 120, 120))

tetrimino = Tetrimino(2)

mino.fill(tetrimino.get_color())

teste = 0

clock = pygame.time.Clock()
direction = 1
# position_x = 3
# position_y = 0

tempo_level = 20
contador = 0

while True:
	clock.tick(15)

	contador += 1
	if contador > tempo_level:
		contador = 0
		# position_y += 1  # temporário

	# inicio teste

	# (color, shape) = tetrimino_giver(teste)
	
	# if direction > 1:
	# 	shape = tetrimino_rotator(shape,direction)
	
	# if direction > 2:
	# 	shape = tetrimino_rotator(shape,direction)
	
	# if direction > 3:
	# 	shape = tetrimino_rotator(shape,direction)
	
	# shape = tetrimino_mover(reshape(shape), 0, 0)

	# mino.fill(color)
	# tetrimino = shape
	# if teste < 6:
	# 	teste+=1
	# else:
	# 	teste=0
	# 	direction+=1

	# if direction > 4:
	# 	direction = 1

	# fim teste

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				quit()
			if event.key == K_UP:
				tetrimino.rotate()
			if event.key == K_RIGHT:
				tetrimino.move_right()
			if event.key == K_LEFT:
				tetrimino.move_left()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.quit()
			quit()

	# ghost = ghost_position(deepcopy(tetrimino.position()))

	screen.fill((0, 0, 0))

	for i in range(10):
		for j in range(20):
			matrix.blit(cell[i][j], grid_position((i, j)))

	for pos in tetrimino.position():
		matrix.blit(mino, grid_position(pos))

	# for pos in ghost:
	# 	matrix.blit(ghost_mino, grid_position(pos))

	screen.blit(matrix, matrix_pos)

	pygame.display.update()
