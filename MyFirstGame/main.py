import pygame

# Инициализация Pygame
pygame.init()

# Параметры экрана и фона
clock = pygame.time.Clock()
screen = pygame.display.set_mode((983, 360))
pygame.display.set_caption("MY First Game")
icon = pygame.image.load('images/icon.webp').convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.jpeg').convert_alpha()

# Загрузка анимаций
walk_left = [
    pygame.image.load('images/player_left/Pasted Graphic 1.png'),
    pygame.image.load('images/player_left/Pasted Graphic 2.png'),
    pygame.image.load('images/player_left/Pasted Graphic 3.png'),
    pygame.image.load('images/player_left/Pasted Graphic 4.png')
]

walk_right = [
    pygame.image.load('images/player_right/Pasted Graphic right_1.png'),
    pygame.image.load('images/player_right/Pasted Graphic right_2.png'),
    pygame.image.load('images/player_right/Pasted Graphic right_3.png'),
    pygame.image.load('images/player_right/Pasted Graphic right_4.png')
]

ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghost_list_in_game = []

# Параметры игрока
player_anim_count = 0
bg_x = 0

player_speed = 15
player_x = 150
player_y = 176
player_direction = "right"  # Направление движения

is_jump = False
jump_count = 10

# Звук фона
bg_sound = pygame.mixer.Sound('sounds/The%20Notorious%20BIG%20%E2%80%93%20Big%20Poppa.mp3')
# bg_sound.play()  # Команда запускает песню

#таймер на создание монстров
ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2500)


label = pygame.font.Font('fonts/Anton-Regular.ttf', 40)
lose_label = label.render('You lose!', False, (193, 196, 199))
restart_label = label.render('Play again!', False, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(380, 190))

bullets_left = 5
bullet = pygame.image.load('images/bullet.png').convert_alpha()
bullets = []

gameplay = True

# Основной цикл игры
running = True
while running:
    # Отрисовка фона
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 983, 0))

    if gameplay:
           player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

           if ghost_list_in_game:
               for (i, el) in enumerate(ghost_list_in_game):
                   screen.blit(ghost, el)
                   el.x -= 10

                   if el.x < -10:
                       ghost_list_in_game.pop(i)

                   if player_rect.colliderect(el):
                       gameplay = False

           # Управление игроком
           keys = pygame.key.get_pressed()
           if keys[pygame.K_LEFT] and player_x > 40:
             player_x -= player_speed
             player_direction = "left"
           elif keys[pygame.K_RIGHT] and player_x < 300:
             player_x += player_speed
             player_direction = "right"

            # Прыжок
           if not is_jump:
               if keys[pygame.K_SPACE]:
                  is_jump = True
                  jump_count = 10
           else:
               if jump_count >= -10:
                  player_y -= (jump_count * abs(jump_count)) * 0.3  # Высота прыжка
                  jump_count -= 1
               else:
                  is_jump = False
                  jump_count = 10

           # Анимация игрока
           if player_anim_count >= len(walk_left) * 3:  # Замедление анимации
                player_anim_count = 0
           if player_direction == "left":
                screen.blit(walk_left[player_anim_count // 3], (player_x, player_y))
           else:
                screen.blit(walk_right[player_anim_count // 3], (player_x, player_y))
                player_anim_count += 1

             # Двигающийся фон
           bg_x -= 2
           if bg_x <= -983:
                bg_x = 0


           if bullets:
               for (i ,el) in enumerate(bullets):
                   screen.blit(bullet, (el.x, el.y))
                   el.x += 4

                   if el.x > 986:
                       bullets.pop(i)

                   if ghost_list_in_game:
                       for (index, ghost_el) in enumerate(ghost_list_in_game):
                           if el.colliderect(ghost_el):
                               ghost_list_in_game.pop(index)
                               bullets.pop(i)
    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (380, 100))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()
            bullets.clear()
            bullets_left = 5

    pygame.display.update()

    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(985, 207)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_e and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 30)))
            bullets_left -= 1

    # Ограничение FPS
    clock.tick(30)
