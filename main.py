import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()

    dt = 0
    gameclock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    newplayer = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    myAsteroidField = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (100,100,255))
        updatable.update(dt)
        if newplayer.shot_timer >= dt:
            newplayer.shot_timer -= dt
        else:
            newplayer.shot_timer = 0
        for obj in asteroids:
            if obj.check_collision(newplayer):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if obj.check_collision(bullet):
                    obj.split(asteroids, updatable, drawable)
                    bullet.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = gameclock.tick(60)/1000

if __name__ == "__main__":
    main()