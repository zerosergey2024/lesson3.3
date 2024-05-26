import pygame
import random
pygame.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Иконка к игре.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width=80
target_height=80

target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint(0,SCREEN_HEIGHT - target_height)

color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

running = True
shots_fired = 0

running = True
shots_fired = 0
game_started = False

while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and shots_fired < 5 and game_started:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                hits += 1
                shots_fired += 1

    screen.blit(target_img, (target_x, target_y))
    show_hits()

    if not game_started:
        start_text = font.render("Press 'S' to Start", True, (0, 0, 0))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))

    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        game_started = True

    if shots_fired == 5:
        game_started = False
        hits = 0
        shots_fired = 0

pygame.quit()


# while running and shots_fired < 5:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and shots_fired < 5:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                shots_fired += 1


    target_x += 1  # Пример непрерывного движения мишени
    if target_x > SCREEN_WIDTH:
        target_x = 0

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()


