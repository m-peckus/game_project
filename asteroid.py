import pygame
import random 
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y,radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
    # Draw a circle on the screen with white color,
    # centered at self.position, with a radius of self.radius
    # and a line thickness of 2
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
    
    def update(self, dt):
    # Calculate change in position using velocity vector and delta time
        displacement = self.velocity * dt
    # Update the position by adding the displacement
        self.position += displacement