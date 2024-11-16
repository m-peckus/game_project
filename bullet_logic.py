def fire_bullet(self,x ,y):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
         #load png image bullet
        bullet = pygame.image.load('/home/mpeckus/game_project/bullet-32_32_pixels.png') .convert_alpha()
    #resize image to fit game scale
        bullet = pygame.transform.scale(bullet, (30, 30))
        bullet_X = 0
    #bullet starting point on Y axis (top to bottom)
        bullet_Y = SCREEN_HEIGHT / 2 
        bullet_X_change = 0
        bullet_Y_change = 10 #bullet speed on Y axis
    #state "ready" can't see the bullet
    #state "fire" bullet is currently moving 
        #bullet_state = "ready" #can't see bullet on the screen
    #global bullet_state
        #bullet_state = "fire"
    #draw bullet on the screen at x and y coordinates
        screen.blit(bullet, (SCREEN_WIDTH / 2 + 16,SCREEN_HEIGHT / 2 + 10))