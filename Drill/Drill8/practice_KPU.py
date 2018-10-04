from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024




def draw_line(p1, p2, p3, p4):
    # fill here
    global character
    global frame

    global x
    global y
    global i

    for i in range(0, 50, 2):
        t = i / 50
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2


    pass

# fill here

size = 10

points = [(random.randint(400, 800), random.randint(400, 800)) for i in range(size)]

n = 1
# fill here
open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame = 0


x = 0
y = 0
i = 0
while True:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    draw_line(points[n-1], points[n],points[n+1],points[n+2])

    character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    frame = (frame + 1) % 8
    if i == 100:
        n = (n+1) % size
        i=0

    update_canvas()



close_canvas()




