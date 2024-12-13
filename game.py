import pygame

pygame.init()

width = 400
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Переверни фишки")

cell_size = width // 4

yellow = (255, 230, 0)
red = (255, 0 ,0)

field = [[random.choice([yellow, red]) for _ in range(4)] for _ in range(4)]
