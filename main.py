# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

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

    #Create two groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #Add groups to containers
    Player.containers = (updatable, drawable)

    #Instantiate Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Setup game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Fill screen with solid black
        screen.fill((0, 0, 0))

        #Update player rotation
        updatable.update(dt)

        #Render player on screen
        for player in drawable:
            player.draw(screen)
 
	#Refresh screen
        pygame.display.flip()

        #Pause gameloop for 1/60th of a second
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
