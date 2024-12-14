import pygame
import random
import sys

pygame.init()

sound = pygame.mixer.Sound('щелчок.mp3')

bg_sound_game = pygame.mixer.Sound('фон.mp3')  
bg_sound_game.set_volume(0.05)

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Переверни фишки")

cell_size = width // 4

yellow = (255, 230, 0)
red = (255, 0 ,0)


def main_game():
    sound = pygame.mixer.Sound('щелчок.mp3')
    field = [[random.choice([yellow, red]) for _ in range(4)] for _ in range(4)]
    
    def change_color (x, y):
        if 0 <= x < 4 and 0 <= y < 4:
            field[x][y] = red if field[x][y] == yellow else yellow
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx = x + i
            dy = y + j
            if 0 <= dx < 4 and 0 <= dy < 4:      # проверка, чтобы не выйти за границы поля
                field[dx][dy] = red if field[dx][dy] == yellow else yellow
    
    running = True
    
    while running:
        for event in pygame.event.get():         # условие для считывания действий пользователя
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid_x = x // cell_size
                grid_y = y // cell_size
                sound.play()                    # для воспроизведения звука при нажатии
                change_color(grid_x, grid_y)
          
        screen.fill((255, 255, 255))
      
        for i in range (4):
            for j in range (4):
                color = field[i][j]
                pygame.draw.circle(screen, color, (i * cell_size + cell_size // 2, j * cell_size + cell_size //2), cell_size // 2 - 5)
    
        all_same = True
        for row in field:
            for cell in row:
                if cell != field[0][0]:
                    all_same = False
                    break
            if not all_same:
                break
    
        if all_same:
            font = pygame.font.Font(None, 50)
            text = font.render("Задача решена!", True, (0, 0, 0))
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    
        pygame.display.flip()    # для обновления экрана
  
pygame.quit()
