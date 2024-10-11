import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    updatable = pygame.sprite.Group() # Objects that can be updated
    drawable = pygame.sprite.Group()  # Objects that can be drawn
    Player.containers = (updatable, drawable)#the containers for the Player class
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #player x, y values imported from constants.py
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # calculate delta time        
        dt = clock.tick(60) / 1000  # limit the framerate to 60 FPS

        # iterates over each sprite in the updatable group, manually calling the update method on each sprite with the same dt argument.
        for sprite in updatable:
            sprite.update(dt)

        # Clear the screen
        screen.fill("black")# Fill with black, or whatever your background color is

        # iterates over each sprite in the drawable group, manually calling the draw method on each sprite with the same screen argument.
        for sprite in drawable:
            sprite.draw(screen)
            
        # Flip the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
    
