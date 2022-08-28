import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Game")
background = pygame.image.load("/Users/hyunwoo/Documents/Python_대회/Main/background.png")
CH_BigBrother = pygame.image.load("/Users/hyunwoo/Documents/Python_대회/Main/BigBrother_CH-.png")
CH_BigBrother_size = CH_BigBrother.get_rect().size
CH_BigBrother_width = CH_BigBrother_size[0]
CH_BigBrother_height = CH_BigBrother_size[1]
CH_BigBrother_x_pos = screen_width / 2
CH_BigBrother_y_pos  = screen_height - CH_BigBrother_height

running = True
while running:
  for event in pygame.event.get():
    screen.blit(background, (0,0))
    screen.blit(CH_BigBrother, (CH_BigBrother_x_pos, CH_BigBrother_y_pos))
    pygame.display.update()
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()

