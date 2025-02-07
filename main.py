# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    #Initialize pygame
    pygame.init()

    #Welcome Message
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Initilize GUI Screen with predefined constant variables for width / height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Setup game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        #Fill screen with solid black
        screen.fill((0, 0, 0))
	
	#Refresh screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
