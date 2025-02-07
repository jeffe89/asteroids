# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    #Initialize pygame
    pygame.init()

    #Welcome Message
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Initilize GUI Screen with predefined constant variables for width / height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Set FPS to 60
    clock = pygame.time.Clock()
    dt = 0

    #Create four groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Add groups to containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    #Instantiate Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Instantiate AsteroidField object
    AsteroidField()

    #Setup game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Fill screen with solid black
        screen.fill((0, 0, 0))

        #Update player rotation
        updatable.update(dt)

        #Check for player collision with asteroid
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                exit()

        #Check for player shot collision with asteroid
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        #Render player on screen
        for obj in drawable:
            obj.draw(screen)
 
	#Refresh screen
        pygame.display.flip()

        #Pause gameloop for 1/60th of a second
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
