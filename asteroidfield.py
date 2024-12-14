import pygame # Import Pygame for game development
import random # Import random for generating random values
from asteroid import Asteroid # Import Asteroid class for creating asteroid objects
from constants import * # Import constants for reusable settings and configurations

# Class to manage the spawning and behavior of asteroids in the game
class AsteroidField(pygame.sprite.Sprite):
    # Defines screen edges for asteroid spawning with corresponding directions and positions
    edges = [
        [
            pygame.Vector2(1, 0), # Spawn from the left edge moving right
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0), # Spawn from the right edge moving left
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1), # Spawn from the top edge moving down
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1), # Spawn from the bottom edge mowing up
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        # Initialize the AsteroidField sprite and set up a spawn timer
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0 # Tracks time between asteroid spawns

    def spawn(self, radius, position, velocity):
        # Create a new asteroid with specified radius, position, and velocity
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity # Assign velocity for asteroid movement

    def update(self, dt):
        # Increment spawn timer by elapsed time
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE: # If time to spawn a new asteroid
            self.spawn_timer = 0 # Reset spawn timer

            # Select a random edge for spawning 
            edge = random.choice(self.edges)
            speed = random.randint(40, 100) # Random speed for the asteroid
            velocity = edge[0] * speed # Set velocity based on the edge direction
            velocity = velocity.rotate(random.randint(-30, 30)) # Add random angle
            position = edge[1](random.uniform(0, 1)) # Random position along the edge
            kind = random.randint(1, ASTEROID_KINDS) # Random asteroid size multiplier
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity) # Spawn asteroid