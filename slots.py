import pygame
import random

pygame.init()

(width, height) = (1300, 800)
screen = pygame.display.set_mode((width,height))
pygame.display.flip()
pygame.display.set_caption("Slots by Kerem & Leon")
bg = pygame.image.load("background1.jpg")
pygame.display.toggle_fullscreen()
screen.blit(bg, (0,0))
pygame.display.update()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


