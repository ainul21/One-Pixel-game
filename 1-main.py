import pygame
import sys
from map import draw_map, map_data
from player import Player

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("One-Pixel RPG Map")

# Create the player
player = Player(map_data)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            player.on_key_press(event.key)

        if event.type == pygame.KEYUP:
            player.on_key_release(event.key)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the map
    draw_map(screen)

    # Update the player
    player.update()
    player.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
