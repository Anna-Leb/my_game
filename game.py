import pygame
import random
import sys

pygame.init()

sound = pygame.mixer.Sound('щелчок.mp3')

bg_sound_game = pygame.mixer.Sound('фон.mp3')  
bg_sound_game.set_volume(0.05)
bg_sound_menu = pygame.mixer.Sound('меню.mp3')  
bg_sound_menu.set_volume(0.05)

button_width, button_height = 200, 50
button_color = (0, 120, 255)
button_hover_color = (0, 150, 255)
button_text_color = (255, 255, 255)

font_size = 30
font = pygame.font.Font(None, font_size)

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Переверни фишки")

cell_size = width // 4

yellow = (255, 230, 0)
red = (255, 0 ,0)

def draw_button(text, x, y):
    button_rect = pygame.Rect(x, y, button_width, button_height)
    mouse_pos = pygame.mouse.get_pos()

    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, button_hover_color, button_rect)
        return button_rect, True
    else:
        pygame.draw.rect(screen, button_color, button_rect)

    label = font.render(text, True, button_text_color)
    text_rect = label.get_rect(center=button_rect.center)
    screen.blit(label, text_rect)

    return button_rect, False

def main_game():
    sound = pygame.mixer.Sound('щелчок.mp3')
    field = [[random.choice([yellow, red]) for _ in range(4)] for _ in range(4)]
    
    bg_sound_menu.stop()
    bg_sound_game.play(-1)
    
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
        
running = True
bg_sound_menu.play(-1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    button1_y = (height - button_height) // 2 - button_height
    button1_rect, button1_hovered = draw_button("Начать игру!", (width - button_width) // 2, button1_y)

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
        if button1_rect.collidepoint(pygame.mouse.get_pos()):
            main_game()

    screen.fill((255, 255, 255))        # метод для очисти экрана
    
pygame.quit()
