#Вариант для клавиатуры
import pygame

pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")
image = pygame.image.load("233.png")
image_rect = image.get_rect()
speed = 1
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        image_rect.x -= speed

    if keys[pygame.K_RIGHT]:
        image_rect.x += speed

    if keys[pygame.K_UP]:
        image_rect.y -= speed

    if keys[pygame.K_DOWN]:
        image_rect.y += speed

    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    pygame.display.flip()
pygame.quit()

#Вариант для мыши
import pygame
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")
image = pygame.image.load("233.png")
image_rect = image.get_rect()
#Скорость удалена!
run = True




while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if event.type == pygame.MOUSEMOTION:
        mouseX, mouseY = pygame.mouse.get_pos()
        image_rect.x = mouseX - 40
        image_rect.y = mouseY - 40


    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    pygame.display.flip()
pygame.quit()

#Взаимодействие может быть разным, в Pygame можно создать много вариантов взаимодействий.
# Мы создадим столкновение с помощью рамок.

import pygame
pygame.init()
import time

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")
image1 = pygame.image.load("233.png")
image_rect1 = image.get_rect()
#Скорость удалена!

image2 = pygame.image.load("2-2.jpg")
image_rect2 = image2.get_rect()

run = True





while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if event.type == pygame.MOUSEMOTION:
        mouseX, mouseY = pygame.mouse.get_pos()
        image_rect.x = mouseX - 40
        image_rect.y = mouseY - 40

    if image_rect1.colliderect(image_rect2):
        print("Произошло столкновение")
        time.sleep(1)
    screen.fill((0, 0, 0))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)
    pygame.display.flip()
pygame.quit()