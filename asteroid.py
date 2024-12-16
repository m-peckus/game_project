import pygame
from pygame import mixer # Import Pygame mixer
import random # Import random module
from constants import * # Import game constants
from circleshape import CircleShape # Parent class for circular shapes

class Asteroid(CircleShape):
    def __init__(self, x, y,radius):
        # Initialize position and radius using the parent class
        super().__init__(x,y, radius)

    def draw(self, screen):
        # Draw the asteroid as a white circle with a 2-pixel border
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
    
    def update(self, dt):
        # Update position based on velocity and time delta
        displacement = self.velocity * dt
        self.position += displacement

    def split(self, screen):
        # Remove asteroid after being hit by a bullet
        self.kill()
       
        if(self.radius <= ASTEROID_MIN_RADIUS):
            # Initialize Pygame mixer
            pygame.mixer.init()
            # Load sound file
            shot_sound = pygame.mixer.Sound('/home/mpeckus/game_project/Explosion_short.wav')
            # Playe the sound file
            shot_sound.play()
        # If asteroid is too small stop further spliting
            return
        else:
            # Calculate new velocities for split asteroids
            random_angle = random.uniform(20, 50)
            rotated_vector1 = self.velocity.rotate(random_angle) # Rotate velocity by a positive angle
            rotated_vector2 = self.velocity.rotate(-random_angle)# Rotate velocity by a negative angle
            new_radius = self.radius - ASTEROID_MIN_RADIUS # Decrease radius for split asteroids
            
            # Create new asteroids at the same position with the new radius and velocities
            new_asteroid1 = Asteroid(self.position, pygame.Vector2(rotated_vector1), new_radius)
            new_asteroid2 = Asteroid(self.position, pygame.Vector2(rotated_vector2), new_radius)
            
            # Assign calculated velocities to new asteroids and increase their speed by 1.2
            new_asteroid1.velocity = rotated_vector1 * 1.2
            new_asteroid2.velocity = rotated_vector2 * 1.2


            
            
