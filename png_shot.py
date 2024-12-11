import pygame # Import Pygame for game development
from constants import * # Import constants for reusable settings
from circleshape import CircleShape # Import base class for circular objects

# Class to define a bullet (shot) object
class Shot(CircleShape):
    def __init__(self, x, y):
        # Initialize bullet with position, radius properies
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # Draw the bullet as a white circle with a thin outline
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Update the bullet's position based on its velocity and time elapsed
        self.position += self.velocity * dt
        