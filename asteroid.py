import pygame
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x 
        self.y = y 
        
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', (self.x, self.y), self.radius, 2)

    def update(self, dt):
        movement = self.velocity * dt
        self.x += movement.x
        self.y += movement.y
