import pygame # Import Pygame library for handling game elements

# Base class for circular game objects, inheriting from Pygame's Sprite class
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # If the class has a 'containers' attribute, initialize using it; else initialize normally
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Initialize the position of the object as a 2D vector    
        self.position = pygame.Vector2(x, y)

        # Initialize the velocity as a 2D vector (default is stationary)
        self.velocity = pygame.Vector2(0, 0)

        # Set the radius of the circular object
        self.radius = radius

    def draw(self, screen):
        # Placeholder method for rendering; to be overridden by subclasses
        pass

    def update(self, dt):
        # Placeholder method for logic updates; to be overridden by subclasses
        pass

    def collides_with(self, other):
        # Check collision with another object based on the distance between centers and their radius
        return self.position.distance_to(other.position) <= self.radius + other.radius
    
        