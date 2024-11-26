import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print ('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while GAME_RUNNING is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entity in updateable:
            entity.update(dt)
        
        for asteroid in asteroids:
            if player.collision(asteroid) is True: 
                print ('Game over!')
                sys.exit()

        screen.fill("black")
        
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()