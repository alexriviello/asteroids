# uses code from the pygame library
import pygame
# imports all the code from the constants.py file
from constants import *

def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:

        # checks if user has closed the window, will exit if so
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             return
        # fill the screen
        pygame.Surface.fill(screen, "black")
        pygame.display.flip()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
