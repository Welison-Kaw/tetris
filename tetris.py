from my_constants import *
from classes.tetrimino import Tetrimino
from classes.matrix import Matrix
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((MAX_X, MAX_Y))

matrix = Matrix(pygame, BLOCK_SIZE, MAX_X)

# teste
matrix.cell[9][19].color = (0xFF, 0xFF, 0x00)
matrix.cell[8][19].color = (0xFF, 0xFF, 0x00)
matrix.cell[9][18].color = (0xFF, 0xFF, 0x00)
matrix.cell[8][18].color = (0xFF, 0xFF, 0x00)

pygame.display.set_caption('Tetris')

mino = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
ghost_mino = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
ghost_mino.fill((120, 120, 120))

tetrimino = Tetrimino(2, matrix)

mino.fill(tetrimino.color)

teste = 0

clock = pygame.time.Clock()
direction = 1

tempo_level = 20
contador = 0

tetrimino.y = 10

is_moving_right = False
is_moving_left = False

while True:
	clock.tick(15)

	contador += 1
	if contador > tempo_level:
		contador = 0
		tetrimino.y += 1

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
				is_moving_right = True
			if event.key == K_LEFT:
				is_moving_left = True

		if event.type == KEYUP:
			if event.key == K_RIGHT:
				is_moving_right = False
			if event.key == K_LEFT:
				is_moving_left = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.quit()
			quit()

	if is_moving_right:
		tetrimino.move_right()
	if is_moving_left:
		tetrimino.move_left()

	screen.fill((0, 0, 0))

	for i in range(10):
		for j in range(20):
			matrix.obj.blit(matrix.cell[i][j].block, matrix.grid_position((i, j)))

	for pos in tetrimino.ghost_position():
		matrix.obj.blit(ghost_mino, matrix.grid_position(pos))

	for pos in tetrimino.position():
		matrix.obj.blit(mino, matrix.grid_position(pos))

	screen.blit(matrix.obj, matrix.pos)

	pygame.display.update()
