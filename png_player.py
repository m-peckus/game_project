import pygame
import math
from circleshape import CircleShape
from constants import *
from png_shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, image, angle=0, timer=0):
        super().__init__(x, y, PLAYER_RADIUS) #radius value set
        self.position = pygame.Vector2(x, y)
        self.x = x
        self.y = y
        self.image = image
        self.angle = 0 #Initial angle in degrees
        self.rotation = 180
        self.timer = 0 #Limit shoot frequency

    def draw(self, screen):
            #Rotate the image
        rotated_image = pygame.transform.rotate(self.image, -self.angle) #negative for Pygame rotation
        rotated_rect = rotated_image.get_rect(center=self.position)
            #Draw rotated image
        screen.blit(rotated_image, rotated_rect)

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.angle)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()#check which keys are currently being held down
        self.timer -= dt

        if keys[pygame.K_a]:# if a is pressed
            self.angle -= 5
            
        if keys[pygame.K_d]:# if d is pressed
            self.angle += 5

        if keys[pygame.K_w]:# if w is pressed
            self.move(dt)

        if keys[pygame.K_s]:# if s is pressed
            self.move(-dt)

        if keys[pygame.K_SPACE]:# if spacebar is pressed
            if(self.timer <= 0):
                self.shoot()
            
    #shoot bullets
    def shoot(self):
        
        adjusted_angle = self.angle - 90
        self.timer = PLAYER_SHOOT_COOLDOWN


        velocity = pygame.math.Vector2(
            PLAYER_SHOOT_SPEED * math.cos(math.radians(adjusted_angle)), 
            PLAYER_SHOOT_SPEED * math.sin(math.radians(adjusted_angle)))

        shot = Shot(self.position.x, self.position.y)
        shot.velocity = velocity

        

