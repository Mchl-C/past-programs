from ursina import *

# Define a custom class that inherits from Entity
class ColoredCube(Entity):
    def __init__(self, position=(0, 0, 0), color=color.white, scale=(1, 1, 1), **kwargs):
        super().__init__(model='cube', position=position, color=color, scale=scale, **kwargs)

        # Additional initialization or custom behavior can be added here
        self.original_color = color  # Store the original color for later use

    # Custom method to change the color of the cube
    def change_color(self, new_color):
        self.color = new_color

    # Custom method to reset the cube's color to the original
    def reset_color(self):
        self.color = self.original_color

    def input(self, key):
        if key == 'w':
            self.position += self.forward

        if key == 'd':
            self.animate('rotation_y', self.rotation_y + 90, duration=.1)

        if key == 'a':
            self.animate('rotation_y', self.rotation_y - 90, duration=.1)



# Initialize the Ursina app
app = Ursina()

# Create instances of the custom ColoredCube class
cube1 = ColoredCube(position=(1, 0, 0), color=color.red)
cube2 = ColoredCube(position=(-1, 0, 0), color=color.blue, scale=(2, 2, 2))

# Example of using the custom method to change color
def input(key):
    if key == 'space':
        cube1.change_color(color.green)  # Change cube1 color to green on space press
    if key == 'r':
        cube1.reset_color()  # Reset cube1 color to original color on 'r' press

# Start the Ursina app
app.run()
