#file is created to experiment with png object loading as game feature
import sys #interact with the Python runtime environment
import pygame #import pygame library

from constants import * #import constants
from png_player import Player #import Player class
from asteroid import Asteroid #import Adsteroid class(handles the properties and behavior of individual asteroids)
from asteroidfield import AsteroidField #responsible for managing a collection or field of asteroids
from png_shot import Shot #import Shot class

    # main function to initialize the game, set up the environment,start the main game loop
def main():
    pygame.init() #This function initializes all imported pygame modules
        # screen creates the main display surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
         
    pygame.display.set_caption('Flying Saucer Game')# sets the title of the window
    Black = (0, 0, 0) # use in drawing operations, such as filling the screen background.
    clock = pygame.time.Clock() # creates a Clock object used to control the frame rate of the game
    
    # loads an image file
    player_image = pygame.image.load('/home/mpeckus/game_project/ufo.png') .convert_alpha()
    #resizes the image to fit game scale
    player_image = pygame.transform.scale(player_image, (90, 120))

    
        #groups of game objects to perform batch operations on multiple sprites at once
    updatable = pygame.sprite.Group() # Objects that can be updated  in terms of their state or behavior each frame (e.g., position, velocity).
    drawable = pygame.sprite.Group()  # Hold all objects that need to be rendered to the screen each frame
    asteroids = pygame.sprite.Group() # Allows to update and draw all asteroids through group operations, rather than addressing each asteroid individually
  
    shots = pygame.sprite.Group() # manages bullet objects, instances of Shot class in png_shot.py allowing for centralized updates and rendering.


    Asteroid.containers = (asteroids, updatable, drawable)#the container for the Asteroid class. Any instance of Asteroid will be automatically added to these groups when it is created.

    Shot.containers = (shots, updatable, drawable)#container for Shot class. Any instance will be added here

    AsteroidField.containers = updatable#the container for the AsteroidField class. Instances of AsteroidField will be automatically added to the updatable group.

    asteroid_field = AsteroidField() #creates an instance of the AsteroidField class, which is now part of the updatable group due to the previous line. Manages a collection of asteroid objects

    Player.containers = (updatable, drawable)#the containers for the Player class. Each Player instance will be updated and drawn.
    
    # creating a new object player from the Player class from png_player.py with initial position at the center of the screen
    #player_image is a visual representation of the player
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2, player_image, angle=0)

    dt = 0 # time elapsed between frames

    #game loop, it will continue running as long as the game is active 
    while True:
        # iterates over all events currently in the event queue such as player interactions and other events, like quitting the game or responding to keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # iterates over each shot object within the shots_group
        for shot in shots:
            shot.update(dt)#the update method of each individual shot is called, with dt passed as a parameter
            shot.draw(screen)# draw method is called, screen passed as parameter

        # iterates over each sprite in the updatable group, manually calling the update method on each sprite with the same dt argument.
        for sprite in updatable:
            sprite.update(dt)
        
        for sprite in asteroids:
            if sprite.collides_with(player):
                #screen turns black
                screen.fill(Black)
                #Initialize pygame font
                pygame.font.init()
                #create a Font object
                font = pygame.font.Font(None, 40)#None for default font, 40 for size
                #Render the message
                text_surface = font.render('Captain! You just crashed :(', True, (255, 255, 255))# White color
                screen.blit(text_surface, (SCREEN_WIDTH / 2.6, SCREEN_HEIGHT / 2))# Position the text at x and y axis on the screen
                pygame.display.flip()# Update the screen
                pygame.time.wait(4000)  # Wait for 4000 milliseconds (4 seconds)
                #sys.exit()
                print("Game over!")
                pygame.quit() #ensure a smooth disposal of Pygame resources
                sys.exit()
            
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
    