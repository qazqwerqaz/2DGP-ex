from pico2d import *
import math
KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    # fill here
    global running
    global mouse_x, mouse_y
    global stop_mouse_x, stop_mouse_y
    global dir_x, dir_y
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x + 17, KPU_HEIGHT - 1 - event.y - 20
        elif event.type == SDL_MOUSEBUTTONDOWN:
            dir_x = 0
            dir_y = 0
            stop_mouse_x = event.x
            stop_mouse_y = KPU_HEIGHT - 1 - event.y
            dir_x = (float)(event.x - x)//20
            dir_y = (float)(KPU_HEIGHT - 1 - event.y - y)//20
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


# fill here
open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
dir_x, dir_y = 0.0, 0.0
stop_mouse_x, stop_mouse_y = 0,0
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw(mouse_x, mouse_y)
    if dir_x == 0:
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    elif dir_x < 0:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif dir_x > 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)


    update_canvas()
    frame = (frame + 1) % 8

    x += dir_x
    y += dir_y

    if 10 >= math.fabs(stop_mouse_x - x):
        dir_x = 0
        dir_y = 0
        x = stop_mouse_x
        y = stop_mouse_y

    delay(0.02)
    handle_events()

close_canvas()




