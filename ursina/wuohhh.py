from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Fix 1: Add lighting
DirectionalLight(direction=(1, -1, -1), intensity=2)
AmbientLight(color=color.light_gray) 

# Fix 2: Add sky
Sky(texture='sky_default')  # Or use 'sky_sunset'

class CastleBlock(Entity):
    def __init__(self, position, texture='brick', color=color.gray):
        super().__init__(
            collider='box',
            collider_visible=True,
            model='cube',
            texture=texture,
            position=position,
            scale=(1.1,1.1,1.1)
        )

def build_castle():
    # Foundation
    for x in range(-10,11):
        for z in range(-10,11):
            CastleBlock((x,0,z), color=color.dark_gray)

    # Walls (4 sides)
    wall_height = 5
    for y in range(wall_height):
        for x in range(-10,11):
            CastleBlock((x,y,-10))  # Back
            CastleBlock((x,y,10))   # Front
        for z in range(-10,11):
            CastleBlock((-10,y,z))  # Left
            CastleBlock((10,y,z))   # Right

    # Towers
    for y in range(wall_height, wall_height+3):
        CastleBlock((-10,y,-10), color=color.red)
        CastleBlock((-10,y,10), color=color.red)
        CastleBlock((10,y,-10), color=color.red)
        CastleBlock((10,y,10), color=color.red)

build_castle()


# Ground
ground = Entity(
    model='plane',
    texture='grass',
    scale=(50,1,50),
    collider='box'
)

# Fix 3: Don't override FirstPersonController's movement
player = FirstPersonController(
    collider = 'box',
    collider_visible = True,
    position=(0,2,0),
    speed=8,
    jump_height=2
)

hand = Entity(
    parent=camera.ui,
    model='cube',
    texture='pistol',
    position=(0.4, -0.4),  # Lower-right
    rotation=(0, 0, -10),  # Tilt slightly
    scale=(0.3, 0.2, 0.1)
)

def update():
    hit_info = raycast(player.position, (0,0,1), distance=2, debug = True)
    if(held_keys["shift"]):
        player.speed = 16
    else:
        player.speed = 8

        
def input(key):
    if key == 'escape':
        application.quit()
    if key == 'v':
        print(player.speed)
        
app.run()
