import pygame
import random

# Define the map dimensions
map_width = 25
map_height = 19

# Initialize the map with all walls
map_data = [[1 for _ in range(map_width)] for _ in range(map_height)]

# Carve out open spaces within the boundary
for y in range(2, map_height - 2):
    for x in range(2, map_width - 2):
        if random.random() < 0.7:  # Adjust the probability as needed
            map_data[y][x] = 0

# Draw the map
def draw_map(screen):
    GRAY = (128, 128, 128)
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, GRAY, (x * 32, y * 32, 32, 32))
