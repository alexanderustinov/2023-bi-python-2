import pyglet


class Game(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_batch = pyglet.graphics.Batch()
        
        img = pyglet.image.load('cube.png')
        self.coords = (0, 0)
        self.speed_value = 3
        self.speeds = (self.speed_value, 0)
        self.cube = pyglet.sprite.Sprite(img, batch=self.main_batch)
        
    def draw(self, _):
        self.clear()
        self.cube.x += self.speeds[0]
        self.cube.y += self.speeds[1]
        if self.cube.x>self.width:
            self.cube.x-=self.width+self.cube.width
        elif self.cube.x<-self.cube.width:
            self.cube.x+=self.width+self.cube.width
        elif self.cube.y>self.height:
            self.cube.y-=self.height+self.cube.height
        elif self.cube.y<-self.cube.height:
            self.cube.y+=self.height+self.cube.height

        self.main_batch.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.UP:
            self.speeds = (0, self.speed_value)
        elif symbol == pyglet.window.key.DOWN:
            self.speeds = (0, -self.speed_value)
        elif symbol == pyglet.window.key.LEFT:
            self.speeds = (-self.speed_value, 0)
        elif symbol == pyglet.window.key.RIGHT:
            self.speeds = (self.speed_value, 0)

        
game = Game(fullscreen=True)
pyglet.clock.schedule_interval(game.draw, interval=1/60)
pyglet.app.run()