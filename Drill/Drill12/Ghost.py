from pico2d import *
import random
import math
import game_framework
import game_world

# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

Degree_TIME_PER_ACTION = 0.01
Degree_ACTION_PER_TIME = 1.0 / Degree_TIME_PER_ACTION
Degree_PER_ACTION = 3.14

Deg_TIME_PER_ACTION = 0.1
Deg_ACTION_PER_TIME = 720 / Deg_TIME_PER_ACTION
Deg_PER_ACTION = 720

class Ghost:

    def __init__(self, x = 400, y = 300, velocity = 1):
        self.image = load_image('animation_sheet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.Bx, self.By = self.x, self.y + PIXEL_PER_METER*3
        self.frame = 0
        self.image.opacify(random.randint(1, 10)/10)
        self.timer = get_time()
        self.degree = 0

    def draw(self):
        if get_time() - self.timer <= 2:
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, Degree_PER_ACTION * Degree_ACTION_PER_TIME * game_framework.frame_time, '', self.x - 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, 0, '', self.x - 25, self.y - 25, 100, 100)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if get_time() - self.timer <= 2:
            pass
        else:
            self.degree += 720 * game_framework.frame_time / 1.0
            self.x = self.Bx + PIXEL_PER_METER*3*math.cos(self.degree * 3.141592 / 180)
            self.y = self.By + PIXEL_PER_METER*3*math.sin(self.degree * 3.141592 / 180)

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
