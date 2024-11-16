import pygame
import sys

#initialize pygame
pygame.init()

#set up the screen
screen = pygame.display.set_mode((640, 480))

class first:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def show(self, dt):
        print(f"Your dt is {dt}")

class second(first):
    def __init__(self, x, y, angle):
        super().__init__(x,y)
        self.angle = angle
        self.position = 55

    def draw(self, screen):
        pygame.draw.circle(screen, (255,0,0), (320, 240), 25)
x = first(2,4)
    #function to handle spacebar press
def on_spacebar():
    x.show(5)
    y = second(3,4,8)
    screen.fill('white')

    y.draw(screen)


    #main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #check for keydown event (when a key is pressed)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                on_spacebar()
    
    pygame.display.update()

