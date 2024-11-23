import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) #radius value set
        self.rotation = 180
        self.shoot_timer = 0

        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()#check which keys are currently being held down

        if keys[pygame.K_a]:# if a is pressed
            self.rotate(-dt)
            
        if keys[pygame.K_d]:# if d is pressed
            self.rotate(dt)

        if keys[pygame.K_w]:# if w is pressed
            self.move(dt) 

        if keys[pygame.K_s]:# if s is pressed
            self.move(-dt)

        if keys[pygame.K_SPACE]:# if spacebar is pressed
            self.shoot()

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        