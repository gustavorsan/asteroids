import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    y = SCREEN_HEIGHT / 2
    x = SCREEN_WIDTH / 2

    updatable  = pygame.sprite.Group()
    drawable   = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    shots      = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x,y)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt) 
        
        for obj in asteroids:
           if obj.is_colliding(player):
               print("Game Over!")
               sys.exit()        
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000
   

if __name__ == "__main__":
    main()