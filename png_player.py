import pygame
import math
from circleshape import CircleShape
from constants import *
from png_shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, image, angle=0):
        super().__init__(x, y, PLAYER_RADIUS) #radius value set
        self.position = pygame.Vector2(x, y)
        self.x = x
        self.y = y
        self.image = image
        self.angle = 0 #Initial angle in degrees
        self.rotation = 180

    def draw(self, screen):
            #Rotate the image
        rotated_image = pygame.transform.rotate(self.image, -self.angle) #negative for Pygame rotation
        rotated_rect = rotated_image.get_rect(center=self.position)
            #Draw rotated image
        screen.blit(rotated_image, rotated_rect)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 
        self.angle += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.angle)
        self.position += forward * PLAYER_SPEED * dt
    
    
    def update(self, dt):
        keys = pygame.key.get_pressed()#check which keys are currently being held down
        
        if keys[pygame.K_a]:# if a is pressed
            self.angle -= 5
            
        if keys[pygame.K_d]:# if d is pressed
            self.angle += 5

        if keys[pygame.K_w]:# if w is pressed
            self.move(dt)

        if keys[pygame.K_s]:# if s is pressed
            self.move(-dt)

        if keys[pygame.K_SPACE]:# if spacebar is pressed
            self.shoot()

    #shoot bullets
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED  
        print("Rotation", self.rotation)   
        #print("Base Vector", pygame.Vector2(0, 1))
        print("Velocity", shot.velocity)

