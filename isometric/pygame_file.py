import pygame
import math

# Initialize PyGame
pygame.init()

# Constants
TILE_WIDTH = 64
TILE_HEIGHT = 32
MAP_WIDTH = 10
MAP_HEIGHT = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Isometric Grid")

image = pygame.image.load("isometric_cube.png").convert_alpha()  # Use convert_alpha to preserve transparency
image = pygame.transform.scale(image, (150,150))

image_with_bg = pygame.Surface(image.get_size(), pygame.SRCALPHA)
image_with_bg.fill((255, 255, 255))
image_with_bg.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
image_with_bg.set_colorkey((255, 255, 255))  

# Function to convert 2D grid coordinates to isometric coordinates
def to_isometric(x, y):
    iso_x = (x - y) * (TILE_WIDTH // 2)
    iso_y = (x + y) * (TILE_HEIGHT // 2)
    return iso_x, iso_y

# Function to draw the isometric grid
def draw_grid():
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            iso_x, iso_y = to_isometric(x, y)
            screen.blit(image_with_bg, (iso_x + SCREEN_WIDTH // 3 + 60, iso_y + SCREEN_HEIGHT // 6 + 4     ))  
            pygame.draw.polygon(screen, GREEN, [
                (iso_x + SCREEN_WIDTH // 2, iso_y + SCREEN_HEIGHT // 4),  # Top
                (iso_x + SCREEN_WIDTH // 2 + TILE_WIDTH // 2, iso_y + SCREEN_HEIGHT // 4 + TILE_HEIGHT // 2),  # Right
                (iso_x + SCREEN_WIDTH // 2, iso_y + SCREEN_HEIGHT // 4 + TILE_HEIGHT),  # Bottom
                (iso_x + SCREEN_WIDTH // 2 - TILE_WIDTH // 2, iso_y + SCREEN_HEIGHT // 4 + TILE_HEIGHT // 2)  # Left
            ], 1)
            
# Main game loop
running = True
while running:
    screen.fill(BLACK)
    draw_grid()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
