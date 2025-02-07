from circleshape import *
from constants import *
import random

#Class for asteroids
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        #If smallest asteroid - remove from screen
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        #if mediu or large asteroid - split into two of the next smallest size
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid1.velocity = new_velocity1
        asteroid2.velocity = new_velocity2
        self.groups()[0].add(asteroid1)
        self.groups()[0].add(asteroid2)
        self.kill()