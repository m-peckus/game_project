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


    #split asteroid if hit by bullet 26/11
    def split(self, screen):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):#if smal asteroid is shot
            print('small asteroid')
            return
        else:
            #if big asteroid is shot
            random_angle = random.uniform(20, 50)
            rotated_vector1 = self.velocity.rotate(random_angle)
            rotated_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position, rotated_vector1, new_radius)
            new_asteroid1
        """
            random_angle = random.uniform(20, 50)
            rotated_vector1 = self.velocity.rotate(random_angle)
            rotated_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            
            print('----------HIT PACKAGE--------')
            print('random angle',random_angle, -random_angle)
            print('big asteroid initial velocity', self.velocity)
            print('new velocity vector-1', rotated_vector1)
            print('new velocity vector-2', rotated_vector2)
            print('old radius',self.radius,'new radius',new_radius)
            print('-------------------------------')
        """
            
