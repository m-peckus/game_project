import pygame
pygame.init()


# Get display info dinamically
display_info = pygame.display.Info()

# Dynamically calculated variales
SCREEN_WIDTH = display_info.current_w
SCREEN_HEIGHT = display_info.current_h

# Previously used static variables
#SCREEN_WIDTH = 1280 
#SCREEN_HEIGHT = 720

# For mobile-like resolutions
#SCREEN_WIDTH = 360
#SCREEN_HEIGHT = 640

"""
Simulate various screen sizes by manually setting SCREEN_WIDTH and SCREEN_HEIGHT to different values.
Test for common resolutions, like:
1280 x 720
1920 x 1080
800 x 600
Mobile-like resolutions(e.g., 360 X 640)

"""

ASTEROID_MIN_RADIUS = 20
ASTEROID_MEDIUM_RADIUS = 40
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200

PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3
SHOT_RADIUS = 5

min_value = 20
max_value = 50