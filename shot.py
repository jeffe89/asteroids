from circleshape import *
from shot import *
from constants import *

#Class for shots fired
class Shot(CircleShape):
    def __init__(self, position, SHOT_RADIUS):
        super().__init__(position[0], position[1], SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)