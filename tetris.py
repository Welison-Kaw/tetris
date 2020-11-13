import pygame
from pygame.locals import *
from copy import copy, deepcopy

def grid_position(t):
	return (t[0]*block_size+t[0]+1,t[1]*block_size+t[1]+2)

def tetrimino_mover(_shape,_column,_line):
	for i in range(len(_shape)):
		_shape[i][0] += _column
		_shape[i][1] += _line
	return _shape

def tetrimino_rotator(_shape,_direction):
	size = len(_shape)
	r = [[0 for j in range(size)] for i in range(size)]
	for i in range(len(_shape)):
		for j in (range(len(_shape[i]))):
			if shape[i][j] == 1:
				r[j][abs(i-size+1)] = 1
	return r

# transforma numa estrutura que o pygame consiga escrever
def reshape(old_shape):
	r = []
	for i in range(len(old_shape)):
		for j in (range(len(old_shape[i]))):
			if old_shape[i][j] == 1:
				r.append([j,i])
	return r

# cria a sombra da peça
def ghost_position(_shape):
	ghost_shape = _shape.copy()
	
	while (ghost_shape[3][1] < 19):
		for i in range(len(ghost_shape)):
			ghost_shape[i][1] += 1

	return ghost_shape

#temp name
def tetrimino_giver(type):

	#shape = north facing

	if type == O_SHAPE:
		color = [255,255,0] #yellow
		shape =	[[1,1]
				,[1,1]]

	if type == I_SHAPE:
		color = [0,191,255] #deep sky blue
		shape =	[[0,0,0,0]
				,[1,1,1,1]
				,[0,0,0,0]
				,[0,0,0,0]]

	if type == T_SHAPE:
		color = [128,0,128] #purple
		shape =	[[0,1,0]
				,[1,1,1]
				,[0,0,0]]

	if type == L_SHAPE:
		color = [255,165,0] #orange
		shape = [[0,0,1]
				,[1,1,1]
				,[0,0,0]]

	if type == J_SHAPE:
		color = [30,50,255] #blue
		shape =	[[1,0,0]
				,[1,1,1]
				,[0,0,0]]

	if type == S_SHAPE:
		color = [0,128,0] #green
		shape =	[[0,1,1]
				,[1,1,0]
				,[0,0,0]]

	if type == Z_SHAPE:
		color = [255,0,0] #red
		shape =	[[1,1,0]
				,[0,1,1]
				,[0,0,0]]

	return (color, shape)

O_SHAPE = 0
I_SHAPE = 1
T_SHAPE = 2
L_SHAPE = 3
J_SHAPE = 4
S_SHAPE = 5
Z_SHAPE = 6

pygame.init()
max_x = 640
max_y = 480
block_size = 20
screen = pygame.display.set_mode((max_x, max_y))

matrix = pygame.Surface((block_size*10+11,block_size*20+22))
matrix.fill((255,255,255))
matrix_pos = ((max_x-(block_size*10+11))/2,15)

# cria cada item cell
cell = []
for i in range(10):
	cell.append([])
	for j in range(20):
		cell[i].append([])
		cell[i][j] = pygame.Surface((block_size, block_size))
		cell[i][j].fill((0,0,0))

pygame.display.set_caption('Tetris')

mino = pygame.Surface((block_size, block_size))
ghost_mino = pygame.Surface((block_size, block_size))
ghost_mino.fill((120,120,120))

(color, shape) = tetrimino_giver(2)

shape = tetrimino_mover(shape, 0, 0)

mino.fill(color)
# tetrimino = reshape(shape)

teste = 0

clock = pygame.time.Clock()
direction = 1
position_x = 3
position_y = 0

tempo_level = 20
contador = 0

while True:
	clock.tick(15)

	contador += 1
	if contador > tempo_level:
		contador = 0
		# position_y += 1 // temporário

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

	#fim teste

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				quit()
			if event.key == K_UP:
				shape = tetrimino_rotator(shape,direction)
				if reshape(shape)[3][0]+position_x > 9:
					position_x = 6
				if reshape(shape)[0][0]+position_x < 0:
					position_x = 0
			if event.key == K_RIGHT:
				if reshape(shape)[3][0]+position_x < 9:
					position_x += 1
			if event.key == K_LEFT:
				if reshape(shape)[0][0]+position_x > 0:
					position_x -= 1

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.quit()
			quit()

	tetrimino = tetrimino_mover(reshape(shape), position_x, position_y)
	ghost = ghost_position(deepcopy(tetrimino))

	screen.fill((0,0,0))

	for i in range(10):
		for j in range(20):
			matrix.blit(cell[i][j], grid_position((i,j)))

	for pos in tetrimino:
		matrix.blit(mino,grid_position(pos))

	for pos in tetrimino:
		matrix.blit(mino,grid_position(pos))

	for pos in ghost:
		matrix.blit(ghost_mino,grid_position(pos))

	screen.blit(matrix, matrix_pos)

	# pygame.draw.rect(screen,(50,50,50),[300,2,100,40])

	pygame.display.update()