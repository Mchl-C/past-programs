import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_isometric_cube(ax, x, y, z, size):
    # Define the 8 vertices of a cube, height of pyramid
    vertices = np.array([[x, y, z],
                         [x + size, y, z],
                         [x + size, y + size, z],
                         [x, y + size, z],
                         [x, y, z + size],
                         [x + size, y, z + size],
                         [x + size, y + size, z + size],
                         [x, y + size, z + size],
                         [size / 2, y / size, z]])  # Pyramid point
    
    # Define the 6 faces of the cube (each face is a list of 4 vertices)
    faces = [[0, 1, 5, 4],  # Front
             [7, 6, 5, 4],  # Top
             [2, 3, 7, 6],  # Back
             [0, 3, 7, 4],  # Left
             [1, 2, 6, 5],  # Right
             [0, 1, 2, 3]]  # Bottom

    # Red signs
    mark_1 = [[5, 6]]

    # Blue signs
    mark_2 = [[0, 2], [2,4]]

    # Green signs
    mark_3 = [[1, 8]]
                        
    # Draw cube sides
    ax.add_collection3d(Poly3DCollection([vertices[face] for face in faces],
                                         facecolors=['lightgrey', 'grey', 'darkgrey', 'dimgray', 'black', 'silver'],
                                         edgecolor='k', linewidths=1, alpha=0.8))
    
    # Draw marked lines
    ax.add_collection3d(Poly3DCollection([vertices[face] for face in mark_1],
                                         facecolors=['white'], edgecolor='r'))
    
    ax.add_collection3d(Poly3DCollection([vertices[face] for face in mark_2],
                                         facecolors=['white'], edgecolor='b'))

    ax.add_collection3d(Poly3DCollection([vertices[face] for face in mark_3],
                                         facecolors=['white'], edgecolor='g'))

    # Annotate each vertex with a number
    for i, vertex in enumerate(vertices):
        ax.text(vertex[0] + 0.05, vertex[1] + 0.05, vertex[2] + 0.05, str(i), color='black', fontsize=15)

# Setup the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Draw the cube
draw_isometric_cube(ax, 0, 0, 0, 1)

# Set the perspective (isometric view angle)
ax.view_init(30, 30)

# Hide the axes
ax.set_axis_off()

# Show the plot
plt.show()
