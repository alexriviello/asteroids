# uses code from the pygame library
import pygame
# imports all the code from the constants.py file
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    # initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    while True:
        # checks if user has closed the window, will exit if so
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             return
        # fill the screen
        screen.fill("black")

        # update everything that's updatable
        for thing in updatable:
            thing.update(dt)
        
        # only draw things that are drawable
        for thing in drawable:
            thing.draw(screen)
    
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                exit("Game over!")
            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
