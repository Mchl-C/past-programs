from ursina import *

app = Ursina()

# Create a cube
cube = Entity(model='cube', color=color.red, scale=(2, 2, 2))

# Animate the cube's position over 2 seconds
cube.animate_position((5, 0, 0), duration=2)

app.run()
