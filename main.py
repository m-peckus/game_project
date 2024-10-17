import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    updatable = pygame.sprite.Group() # Objects that can be updated
    drawable = pygame.sprite.Group()  # Objects that can be drawn
    asteroids = pygame.sprite.Group() # asteroid objects


    Asteroid.containers = (asteroids, updatable, drawable)#the container for the Asteroid class
    AsteroidField.containers = updatable#the container for the AsteroidField class
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)#the containers for the Player class
    
    #Player class values imported from constants.py
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    dt = 0

    
    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
               

        # iterates over each sprite in the updatable group, manually calling the update method on each sprite with the same dt argument.
        for sprite in updatable:
            sprite.update(dt)
        
        for sprite in asteroids:
            #player.is_colliding(sprite)
            if(player.is_colliding(sprite)):
                print('collision detected!')
                sys.exit("spaceship crashed :(")
            else:
                print('no collision')
        # Clear the screen
        screen.fill("black")# Fill with black, or whatever your background color is

        # iterates over each sprite in the drawable group, manually calling the draw method on each sprite with the same screen argument.
        for sprite in drawable:
            sprite.draw(screen)
            
        # Flip the display
        pygame.display.flip()
        
        # calculate delta time 
        dt = clock.tick(60) / 1000  # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()
    
