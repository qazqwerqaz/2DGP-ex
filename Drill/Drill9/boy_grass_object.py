from pico2d import *
import random

# Game object class here
class boy:
    def __init__(self):
        self.x, self.y = 100, 90
        self.flame = 0
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.flame = (self.flame+1)%8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.flame*100, 100, 100, 100, self.x, self.y)
    pass

class Grass:
    def __init__(self):
        self.x ,self.y = 0, 90
        self.image = load_image('grass.png')


    def draw(self):
        self.image.draw(400, 30)
    pass

class ball:

    def __init__(self):
        self.x, self.y = random.randint(0, 800) , 0
        a = random.randint(0, 1)
        if a == 1:
            self.image = load_image('ball21x21.png')
        elif a == 0:
            self.image = load_image('ball41x41.png')


    def update(self):
        self.y += 5

    def draw(self):
        self.image.draw(self.x, self.y)
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

boy1 = [boy()]*20
grass = Grass()
ball_ = [ball()]*20
running = True

# game main loop code

while running:
    handle_events()


    for boy in boy1:
        boy.update()

    for ball in ball_:
        ball_.update()

    clear_canvas()
    grass.draw()

    for ball in ball_:
        ball_.update()
    for boy in boy1:
        boy.draw()
    update_canvas()

    delay(0.05)

close_canvas()
# finalization code