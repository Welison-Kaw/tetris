import pygame
from pygame.locals import *

def grid_position(t):
	return (t[0]*block_size+t[0]+1,t[1]*block_size+t[1]+2)

#temp name
def tetrimino_giver(type):

	if type == O_SHAPE:
		color = (255,255,0) #yellow
		shape =	((0,0)
				,(0,1)
				,(1,0)
				,(1,1))

	if type == I_SHAPE:
		color = (173,216,230) #light blue
		shape =	((0,0)
				,(0,1)
				,(1,0)
				,(1,1))

	if type == T_SHAPE:
		color = (128,0,128) #purple
		shape =	((0,0)
				,(0,1)
				,(1,0)
				,(1,1))

	if type == L_SHAPE:
		color = (255,165,0) #orange
		shape = ((0,0)
				,(0,1)
				,(0,2)
				,(1,2))

	if type == J_SHAPE:
		color = (0,0,139) #dark blue
		shape =	((0,0)
				,(0,1)
				,(1,0)
				,(1,1))

	if type == S_SHAPE:
		color = (0,128,0)
		shape =	((0,0)
				,(0,1)
				,(1,0)
				,(1,1))

	if type == Z_SHAPE:
		color = (255,0,0)
		shape =	((0,0)
				,(0,1)
				,(1,0)
				,(1,1))

	return (color, shape)



# def tetrimino_l(type):
# 	if type == COLOR:
# 		return (255,165,0)
# 	if type == SHAPE:
# 		return ((0,0)
# 			   ,(0,1)
# 			   ,(0,2)
# 			   ,(1,2))

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

print(grid_position((1,2)))

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

(color, shape) = tetrimino_giver(0)

mino.fill(color)
tetrimino = shape

teste = 0

clock = pygame.time.Clock()

while True:
	clock.tick(1)

	(color, shape) = tetrimino_giver(teste)

	mino.fill(color)
	tetrimino = shape
	if teste < 6:
		teste+=1
	else:
		teste=0


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

	for i in range(10):
		for j in range(20):
			# matrix.blit(cell[i][j], (i*block_size+i+1,j*block_size+j+2))
			matrix.blit(cell[i][j], grid_position((i,j)))

	for pos in tetrimino:
		# print(pos*block_size)
		matrix.blit(mino,grid_position(pos))

	screen.blit(matrix, matrix_pos)

	# pygame.draw.rect(screen,(50,50,50),[300,2,100,40])

	pygame.display.update()