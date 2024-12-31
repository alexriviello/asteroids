# uses code from the pygame library
import pygame
# imports all the code from the constants.py file
from constants import *
from player import *

def main():
    # initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # checks if user has closed the window, will exit if so
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             return
        # fill the screen
        screen.fill("black")

        for thing in updatable:
            thing.update(dt)
            thing.draw(screen)
 
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
