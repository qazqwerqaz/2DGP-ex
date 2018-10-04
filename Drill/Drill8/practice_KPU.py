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

    t=0
    t = i / 100
    x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
    y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
    i=i+1

    pass

# fill here

size = 20

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
    draw_line(points[n], points[(n+1)%size+1],points[(n+2)%size+1],points[(n+3)%size+1])

    character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    for a in range(0, n, 1):

        character.clip_draw(1 * 100, 100 * 3, 100, 100, points[a+3][0],points[a+3][1])
    frame = (frame + 1) % 8
    if i == 100:
        n = (n+1) % 16
        i=0


    update_canvas()



close_canvas()




