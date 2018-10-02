from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024




def draw_line(p1, p2):
    # fill here

    frame = 0
    character.clip_draw(frame * 100, 100 * 3, 100, 100, p1, p2)

    for i in range(0, 100+1, 10):
        t = i / 100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        #draw_point((x,y))
        frame = (frame + 1) % 8

    #draw_point(p2)
    pass

# fill here

size = 10
points = [(random.randint(-500, 500), random.randint(-350, 350)) for i in range(size)]

n = 1
# fill here
open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


while True:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
   # draw_line(points[n-1], points[n])
    n = (n+1) % size

    update_canvas()



close_canvas()




