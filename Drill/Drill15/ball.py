import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(100, 1600-1), random.randint(100, 1000-1), 0
        self.w = 0
        self.h = 0

    def get_bb(self):
        return self.x - self.w - 10, self.y - self.h - 10, self.x - self.w + 10, self.y - self.h + 10

    def set_background(self, bg, back):
        self.bhh = back;
        self.bg = bg
        self.w = self.bg.x
        self.h = self.bg.y

    def draw(self):
        self.image.draw(self.x - self.w, self.y - self.h)
        draw_rectangle(*self.get_bb())


    def update(self):
        pass

