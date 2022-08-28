import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Game")
background = pygame.image.load("/Users/hyunwoo/Documents/Python_대회/Main/background.png")

running = True
while running:
  for event in pygame.event.get():
    screen.blit(background, (0,0))
    pygame.display.update()
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()

