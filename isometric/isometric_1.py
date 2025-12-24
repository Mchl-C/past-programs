import pygame
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Initialize PyGame
pygame.init()

# Constants
TILE_WIDTH = 64
TILE_HEIGHT = 32
MAP_WIDTH = 10
MAP_HEIGHT = 10
CUBE_SIZE = 64
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
DARK_GREY = (100, 100, 100)
LIGHT_GREY = (180, 180, 180)
MEDIUM_GREY = (150, 150, 150)

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Isometric Rendering Example")

# Function to convert 2D grid coordinates to isometric coordinates
def to_isometric(x, y):
    iso_x = (x - y) * (TILE_WIDTH // 2)
    iso_y = (x + y) * (TILE_HEIGHT // 2)
    return iso_x, iso_y

# Function to draw a simple isometric cube using polygon drawing
def draw_isometric_cube(screen, x, y, size):
    iso_x, iso_y = to_isometric(x, y)
    
    # Calculate the points for the top, left, and right faces of the cube
    top = [
        (iso_x + SCREEN_WIDTH // 2, iso_y + SCREEN_HEIGHT // 4),
        (iso_x + SCREEN_WIDTH // 2 + size // 2, iso_y + SCREEN_HEIGHT // 4 - size // 4),
        (iso_x + SCREEN_WIDTH // 2 + size, iso_y + SCREEN_HEIGHT // 4),
        (iso_x + SCREEN_WIDTH // 2 + size // 2, iso_y + SCREEN_HEIGHT // 4 + size // 4)
    ]
    
    left = [
        (iso_x + SCREEN_WIDTH // 2, iso_y + SCREEN_HEIGHT // 4),
        (iso_x + SCREEN_WIDTH // 2 - size // 2, iso_y + SCREEN_HEIGHT // 4 + size // 4),
        (iso_x + SCREEN_WIDTH // 2 - size // 2, iso_y + SCREEN_HEIGHT // 4 + size // 4 + size // 2),
        (iso_x + SCREEN_WIDTH // 2, iso_y + SCREEN_HEIGHT // 4 + size // 2)
    ]
    
    right = [
        (iso_x + SCREEN_WIDTH // 2 + size // 2, iso_y + SCREEN_HEIGHT // 4 + size // 4),
        (iso_x + SCREEN_WIDTH // 2 + size, iso_y + SCREEN_HEIGHT // 4),
        (iso_x + SCREEN_WIDTH // 2 + size, iso_y + SCREEN_HEIGHT // 4 + size // 2),
        (iso_x + SCREEN_WIDTH // 2 + size // 2, iso_y + SCREEN_HEIGHT // 4 + size // 4 + size // 2)
    ]
    
    # Draw each face of the cube with different shades
    pygame.draw.polygon(screen, LIGHT_GREY, top)  # Top face
    pygame.draw.polygon(screen, MEDIUM_GREY, left)  # Left face
    pygame.draw.polygon(screen, DARK_GREY, right)  # Right face

# Function to draw the isometric grid and cubes
def draw_grid_and_cubes():
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            draw_isometric_cube(screen, x, y, CUBE_SIZE)

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    draw_grid_and_cubes()  # Draw the grid and cubes
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
