from PIL import Image, ImageDraw

# Create an empty image with a white background
width, height = 300, 300
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Define cube size
cube_size = 50

# Define the coordinates of the top face (isometric projection)
top_face = [
    (150, 100),  # Top point
    (150 + cube_size, 100 + cube_size // 2),  # Right point
    (150, 100 + cube_size),  # Bottom point
    (150 - cube_size, 100 + cube_size // 2),  # Left point
]

# Define the coordinates of the left face
left_face = [
    (150 - cube_size, 100 + cube_size // 2),  # Top-left
    (150, 100 + cube_size),  # Bottom-left
    (150, 100 + 2 * cube_size),  # Bottom-right
    (150 - cube_size, 100 + 1.5 * cube_size),  # Top-right
]

# Define the coordinates of the right face
right_face = [
    (150 + cube_size, 100 + cube_size // 2),  # Top-right
    (150, 100 + cube_size),  # Bottom-left
    (150, 100 + 2 * cube_size),  # Bottom-right
    (150 + cube_size, 100 + 1.5 * cube_size),  # Top-left
]

# Fill the faces with different shades to simulate light and depth
draw.polygon(top_face, fill=(180, 180, 180))  # Light grey for the top face
draw.polygon(left_face, fill=(150, 150, 150))  # Darker grey for the left face
draw.polygon(right_face, fill=(100, 100, 100))  # Darkest grey for the right face

# Save the image
image.save("isometric_cube.png")
image.show()
