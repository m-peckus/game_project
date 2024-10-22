#file is created to experiment with png object loading as game feature
import pygame
from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    #image value added 21-10, can delete later on
    def __init__(self, x, y, image):
        super().__init__(x, y, PLAYER_RADIUS) #radius value set
        #suspended on 20-10
        #self.rotation = 180
        self.angle = 0
        #made self.angle and self.image 20-10, can delete later on
        self.image = image

        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        #method body suspended on 21 -10 , for trying to load image
        #pygame.draw.polygon(screen, 'white', self.triangle(), 2)

        # added on 21 -10
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        # added on 21 -10
        new_rect = rotated_image.get_rect(center=self.position)
        # added on 21 -10
        screen.blit(rotated_image, new_rect.topleft)

    #cool rgb values Cosic Blue: (0, 191, 255)  Martian Red: (255, 69, 0) Alien Green: (57, 255, 20) Solar Gold: (255, 215, 0)
    #
    
    def rotate(self, dt):
        #suspended 21-10
        #self.rotation += PLAYER_TURN_SPEED * dt 
        self.angle += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.angle)
        self.position -= forward * PLAYER_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()#check which keys are currently being held down

        if keys[pygame.K_a]:# if a is pressed
            self.rotate(-dt)
            
        if keys[pygame.K_d]:# if d is pressed
            self.rotate(dt)

        if keys[pygame.K_w]:# if w is pressed
            self.move(dt) 

        if keys[pygame.K_s]:# if s is pressed
            self.move(-dt)

