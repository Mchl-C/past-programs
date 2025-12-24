import cairo

# Image settings
width, height = 300, 300

# Create a surface and context for drawing
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Set background color
context.set_source_rgb(1, 1, 1)  # White background
context.paint()

# Function to draw an isometric cube
def draw_isometric_cube(ctx, x, y, size):
    # Define coordinates of the top face
    top = [(x, y), (x + size, y - size * 0.5), (x + size * 2, y), (x + size, y + size * 0.5)]
    
    # Define coordinates of the left face
    left = [(x, y), (x, y + size), (x + size, y + size * 1.5), (x + size, y + size * 0.5)]
    
    # Define coordinates of the right face
    right = [(x + size, y + size * 0.5), (x + size * 2, y), (x + size * 2, y + size), (x + size, y + size * 1.5)]
    
    # Draw and fill the top face
    ctx.move_to(*top[0])
    for point in top[1:]:
        ctx.line_to(*point)
    ctx.close_path()
    ctx.set_source_rgb(0.8, 0.8, 0.8)  # Light grey
    ctx.fill()
    
    # Draw and fill the left face
    ctx.move_to(*left[0])
    for point in left[1:]:
        ctx.line_to(*point)
    ctx.close_path()
    ctx.set_source_rgb(0.6, 0.6, 0.6)  # Medium grey
    ctx.fill()
    
    # Draw and fill the right face
    ctx.move_to(*right[0])
    for point in right[1:]:
        ctx.line_to(*point)
    ctx.close_path()
    ctx.set_source_rgb(0.4, 0.4, 0.4)  # Dark grey
    ctx.fill()

# Draw the cube
draw_isometric_cube(context, 100, 150, 50)

# Save the image to a file
surface.write_to_png("isometric_cube_pycairo.png")
print('Done')
