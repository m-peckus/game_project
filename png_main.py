#!/usr/bin/env python3
# Shebang line to make the script executable

# Import necessary modules and classes
import sys # Interact with the Python runtime environment
import pygame # Import pygame for game development
from constants import * # Import constants (e.g., screen size, dimension variables, speed variables)
from png_player import Player # Player class for spaceship behavior
from png_asteroid import Asteroid # Asteroid class for asteroid behavior
from png_asteroidfield import AsteroidField # Manages a collection of asteroids
from png_shot import Shot # Shot class for bullets fired by the player

# Main function: Initializes the game and starts the main game loop
def main():
    pygame.init() # Initializes pygame  module

    # Set up the display    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Flying Saucer Game') # Set window title 
         
    # Define basic game settings
    Black = (0, 0, 0) # Background color 
    clock = pygame.time.Clock() # Control frame rate
    
    # Load and scale player image
    player_image = pygame.image.load('/home/mpeckus/game_project/ufo.png') .convert_alpha() # Load spaceship image
    player_image = pygame.transform.scale(player_image, (90, 120)) # Resize image

    # Create sprite groups for efficient updates and rendering    
    updatable = pygame.sprite.Group() # Sprites with behavior to update
    drawable = pygame.sprite.Group()  # Sprites to be drawn
    asteroids = pygame.sprite.Group() # Group for all asteroids
    shots = pygame.sprite.Group() # Group for bullets
    
    # Assign sprite groups to relevant classes
    Asteroid.containers = (asteroids, updatable, drawable) # Asteroids added to these groups 
    Shot.containers = (shots, updatable, drawable) # Shots added to these groups 
    AsteroidField.containers = updatable # Asteroid field updates itself
    Player.containers = (updatable, drawable) # Player added to drawable and updatable groups 

    # Create asteroid field and player instance
    asteroid_field = AsteroidField() # Spawn a field of asteroids
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2, player_image, angle=0) # Spawn player in the center

    dt = 0 # Time between frames for smooth movement

    # Main game loop
    while True:
        # Handle events (e.g., quit or key presses)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the player closes the window 
                return # Exit the game loop
                
        # Update and draw all bullets
        for shot in shots:
            shot.update(dt) # Update bullet position
            shot.draw(screen) # Draw bullet to the screen

        # Update all updatable sprites
        for sprite in updatable:
            sprite.update(dt)
        
        # Check collision between bullets and asteroids
        for sprite in asteroids:
            for shot in shots:
                if sprite.collides_with(shot): # If a bullet hits an asteroid
                    sprite.split(screen) # Split the asteroid into smaller pieces
                    shot.kill() # Remove the bullet

        # Check collisions between asteroids and the player
        for sprite in asteroids:
            if sprite.collides_with(player):
                # Display crash message
                screen.fill(Black) # Fill screen with black
                pygame.font.init() # Initialize font module
                font = pygame.font.Font(None, 40) # Create font object
                text_surface = font.render('Captain! You just crashed :(', True, (255, 255, 255)) # Create crash message
                screen.blit(text_surface, (SCREEN_WIDTH / 2.6, SCREEN_HEIGHT / 2)) # Position text
                pygame.display.flip() # Update the display
                pygame.time.wait(4000) # Wait 4 seconds before exiting
                print("Game over!")
                pygame.quit() # Clean up pygame resources
                sys.exit() # Exit the script
            
        # Clear the screen for the next frame
        screen.fill("black") # Fill screen with background color

        # Draw all drawable sprites
        for sprite in drawable:
            sprite.draw(screen)
            
        # Update the display
        pygame.display.flip()
        
        # Calculate time between frames to maintain consistent frame rate
        dt = clock.tick(60) / 1000  # Limit the framerate to 60 FPS, calculate delta time

# Run the game when the script is executed
if __name__ == "__main__":
    main()

""" 
Key Blocks with Descriptions:

1. Imports: Import necessary modules and game-specific classes.
2. Game Initialization: Initialize pygame, set up display, and configure game settings.
3. Sprite Groups: Organize game objects into groups for batch updates and rendering.
4. Game Loop:
    * Handle events(e.g, quit the game).
    * Update and draw bullets and sprites.
    * Check collisions and handle asteroid splitting or game over.
    * Clear the screen and redraw objects for the next frame.
5. Exit Conditions: Handle clean game exit and resource cleanup.

"""
    