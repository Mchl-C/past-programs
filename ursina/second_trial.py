from ursina import *

app = Ursina()

class Player(Entity):
    def __init__(self, position=(0,0,0), color = color.white, scale = (1,1,1), **kwargs):
        super().__init__(model='cube', position = position, color = color, scale = scale, **kwargs)

    def input(self, key):
        if key == 'a':
            self.x -= 1 * time.dt
        if key == 's':
            self.y += 1 * time.dt
        if key == 'w':
            self.y -= 1 * time.dt
        if key == 'd':
            self.x += 1 * time.dt

player1 = Player(position = (0,0,0))
app.run()
