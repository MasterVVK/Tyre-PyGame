import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Домашний тир")
icon = pygame.image.load("PICs/free-icon-shooting-range-2689911.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("PICs/target.png")
target_width = 50
target_height = 50
target_img = pygame.transform.scale(target_img, (target_width, target_height))
target_x = random.randint(0,SCREEN_WIDTH - target_width )
target_y = random.randint(0,SCREEN_HEIGHT - target_height)

color_bg = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
#print(color_bg)
#pygame.display.flip()
#pygame.display.update()

running = True
while running:
    screen.fill(color_bg)
    screen.blit(target_img,(target_x, target_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                color_bg_click = (255, 0, 0)
                screen.fill(color_bg_click)
                pygame.display.update()
                time.sleep(0.1)
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

            #print(mouse_x,mouse_y)


pygame.quit()

