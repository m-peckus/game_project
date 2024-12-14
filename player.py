import pygame # Import Pygame library
import math # Import math for trigonometric functions
from circleshape import CircleShape # Import CircleShape as the base class for the Player
from constants import * # Import constants (e.g., PLAYER_SPEED,PLAYER_RADIUS)
from shot import Shot # Import Shot class for shooting bullets

class Player(CircleShape): # Player class inherits from CircleShape
    def __init__(self, x, y, image, angle=0, timer=0):
        # Initialize the base CircleShape class with the palyer's position and radius
        super().__init__(x, y, PLAYER_RADIUS)

        # Set the player's initial position as a 2D vector
        self.position = pygame.Vector2(x, y)

        # Store x and y coordinates for reference
        self.x = x
        self.y = y

        # Load the player's image for visual representation
        self.image = image

        # Initialize the player's orientation (angle) and rotation direction
        self.angle = 0 # Initial angle in degrees
        self.rotation = 180 # Used for rotation (e.g., if player spins)

        # Initialize the timer to control shooting frequency
        self.timer = 0 

    def draw(self, screen):
        # Rotate the player's image based on the current angle
        rotated_image = pygame.transform.rotate(self.image, -self.angle) # Negative angle due to Pygame's rotation system

        # Get the bounding rectangle of the rotated image, centered on the player's position
        rotated_rect = rotated_image.get_rect(center=self.position)
            
        # Draw the rotated image on the screen at the calculated position
        screen.blit(rotated_image, rotated_rect)

    def move(self, dt):
        # Calculate the forward direction vector based on the current angle
        forward = pygame.Vector2(0, -1).rotate(self.angle) # Start with 'up' direction and rotate by the angle
        
        # Update the player's position by moving it forward (or backward if dt is negative)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed() # Check which keys are currently being held down

        # Decrease the timer to allow shooting after cooldown
        self.timer -= dt
        
        # Handle rotation
        if keys[pygame.K_a]: # If 'a' is pressed rotate left
            self.angle -= 5
            
        if keys[pygame.K_d]: # If 'd' is pressed rotate right
            self.angle += 5
        
        # Handle movement
        if keys[pygame.K_w]: # If 'w' is pressed move forward
            self.move(dt)

        if keys[pygame.K_s]: # If 's' is pressed move backward
            self.move(-dt)
        
        # Handle shooting
        if keys[pygame.K_SPACE]: # If SPACE is pressed fire bullets
            if(self.timer <= 0):
                self.shoot()
        

        # Screen wrapping logic
        if self.position.x > SCREEN_WIDTH: # If the player moves off the right edge, wrap to the left
            self.position.x = 0
        elif self.position.x < 0: # If the player moves off the left edge, wrap to the right
            self.position.x = SCREEN_WIDTH
        
        if self.position.y > SCREEN_HEIGHT: # If the player moves off the bottom edge, wrap to the top
            self.position.y = 0
        elif self.position.y < 0: # If the player moves off the top edge, wrap to the bottom
            self.position.y = SCREEN_HEIGHT
        
            
    def shoot(self):
        # Adjust the angle to match the player's orientation
        adjusted_angle = self.angle - 90

        # Reset the shooting cooldown timer
        self.timer = PLAYER_SHOOT_COOLDOWN

        # Calculate the velocity vector for the bullet based on the player's angle
        velocity = pygame.math.Vector2(
            PLAYER_SHOOT_SPEED * math.cos(math.radians(adjusted_angle)), 
            PLAYER_SHOOT_SPEED * math.sin(math.radians(adjusted_angle)))

        # Assign the calculated velocity to the bullet
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = velocity

        

