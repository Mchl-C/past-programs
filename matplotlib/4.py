import pygame
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
import io
from PIL import Image
from mpl_toolkits.mplot3d import proj3d

# Initialize Pygame
pygame.init()

# Pygame settings
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('3D Interactive Cube')

# Function to draw an isometric cube using Matplotlib
def draw_isometric_cube(ax, size, clicked_points):
    # Define the vertices of a cube
    vertices = np.array([[0, 0, 0],
                         [size, 0, 0],
                         [size, size, 0],
                         [0, size, 0],
                         [0, 0, size],
                         [size, 0, size],
                         [size, size, size],
                         [0, size, size]])

    # Define the 6 faces of the cube (each face is a list of 4 vertices)
    faces = [[0, 1, 5, 4],  # Front
             [7, 6, 5, 4],  # Top
             [2, 3, 7, 6],  # Back
             [0, 3, 7, 4],  # Left
             [1, 2, 6, 5],  # Right
             [0, 1, 2, 3]]  # Bottom

    # Draw cube faces
    ax.add_collection3d(Poly3DCollection([vertices[face] for face in faces],
                                         facecolors=['lightgrey', 'grey', 'darkgrey', 'dimgray', 'black', 'silver'],
                                         edgecolor='k', linewidths=1, alpha=0.6))

    # Add points at clicked locations
    if clicked_points:
        for point in clicked_points:
            ax.scatter(point[0], point[1], point[2], color='red', s=100)

# Function to convert Matplotlib figure to a Pygame surface
def get_surface_from_plot(ax, fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image = Image.open(buf)
    mode = image.mode
    size = image.size
    data = image.tobytes()
    return pygame.image.fromstring(data, size, mode)

# Function to find the closest vertex to the click event
def find_closest_vertex(cube_vertices, click_x, click_y):
    min_dist = float('inf')
    closest_vertex = None
    
    for vertex in cube_vertices:
        proj = proj3d.proj_transform(vertex[0], vertex[1], vertex[2], ax.get_proj())
        x2d, y2d, _ = proj[:3]
        dist = np.sqrt((x2d - click_x) ** 2 + (y2d - click_y) ** 2)
        if dist < min_dist:
            min_dist = dist
            closest_vertex = vertex

    return closest_vertex

# Main loop settings
running = True
clock = pygame.time.Clock()
rotation_angle = 0
clicked_points = []

# Main Pygame loop
while running:
    screen.fill((255, 255, 255))

    # Create a Matplotlib figure
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Rotate the cube
    ax.view_init(30, rotation_angle)
    rotation_angle += 1  # Rotate continuously

    # Draw the cube and clicked points
    draw_isometric_cube(ax, size=1, clicked_points=clicked_points)

    # Convert the Matplotlib plot to a Pygame surface
    matplotlib_surface = get_surface_from_plot(ax, fig)

    # Blit the surface onto the Pygame screen
    screen.blit(matplotlib_surface, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Convert mouse position to 3D projection
            mouse_pos = pygame.mouse.get_pos()
            clicked_points.append((np.random.rand(), np.random.rand(), np.random.rand()))

    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
