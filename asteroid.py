from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
        direction = pygame.Vector2()
        random_angle = random.uniform(0, 360)
        direction.from_polar((10, random_angle))
        self.velocity = direction * 3
            
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self, asteroid_group, updatable_group, drawable_group):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        new_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_angle_1 = self.velocity.copy()
        new_ast_1.velocity = new_angle_1.rotate(new_angle) * 1.2
        new_ast_1.add(asteroid_group, updatable_group, drawable_group)
        
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_angle_2 = self.velocity.copy()
        new_ast_2.velocity = new_angle_2.rotate(-new_angle) * 1.2
        new_ast_2.add(asteroid_group, updatable_group, drawable_group)

        self.kill()