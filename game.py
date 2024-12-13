import pygame
import random

pygame.init()

width = 400
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Переверни фишки")

cell_size = width // 4

yellow = (255, 230, 0)
red = (255, 0 ,0)

field = [[random.choice([yellow, red]) for _ in range(4)] for _ in range(4)]

running = True

while running:
  
  for event in pygame.event.get():    # условие для считывания действий пользователя
    if event.type == pygame.QUIT:
      running == False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      x, y = pygame.mouse.get_pos()
            grid_x = x // cell_size
            grid_y = y // cell_size

  for i in range (4):
    for j in range (4):
      color = field[i][j]
      pygame.draw.circle(screen, color, (i * cell_size + cell_size // 2, y * cell_size + cell_size //2), cell_size // 2 - 5)
  screen.fill((255, 255, 255))
  
  pygame.display.flip()    # для обновления экрана
  
pygame.quit()
