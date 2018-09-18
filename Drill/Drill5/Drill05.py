from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# fill here
def move_a_to_b():
    ax, ay, bx, by=203, 535, 132, 243
    frame=0
    character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
    character.clip_draw(frame * 100, 0, 100, 100, bx, by)
    delta_x = (ax - bx)//10
    delta_y = (ay-by)//10
    while(ax >= bx):
        ax -=  delta_x
        ay -=  delta_y
        clear_canvas()
        if delta_x > 0:
            character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, ax, ay)

        update_canvas()
        frame=(frame+1)%8
        delay(0.01)

def move_b_to_c():
    ax, ay, bx, by = 132, 243, 535, 470
    frame = 0
    character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
    character.clip_draw(frame * 100, 0, 100, 100, bx, by)
    delta_x = (ax - bx) // 10
    delta_y = (ay - by) // 10
    while (ax <= bx):
        ax -= delta_x
        ay -= delta_y
        clear_canvas()
        if delta_x > 0:
            character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, ax, ay)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)


def move_c_to_d():
    ax, ay, bx, by = 535, 470, 477, 203
    frame = 0
    character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
    character.clip_draw(frame * 100, 0, 100, 100, bx, by)
    delta_x = (ax - bx) // 10
    delta_y = (ay - by) // 10
    while (ax >= bx):
        ax -= delta_x
        ay -= delta_y
        clear_canvas()
        if delta_x > 0:
            character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, ax, ay)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)


def move_d_to_e():
    ax, ay, bx, by = 477, 203, 715, 136
    frame = 0
    character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
    character.clip_draw(frame * 100, 0, 100, 100, bx, by)
    delta_x = (ax - bx) // 10
    delta_y = (ay - by) // 10
    while (ax <= bx):
        ax -= delta_x
        ay -= delta_y
        clear_canvas()
        if delta_x > 0:
            character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, ax, ay)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)
    pass

def move_e_to_f():
    ax, ay, bx, by = 715, 136, 316, 225
    frame = 0
    character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
    character.clip_draw(frame * 100, 0, 100, 100, bx, by)
    delta_x = (ax - bx) // 10
    delta_y = (ay - by) // 10
    while (ax >= bx):
        ax -= delta_x
        ay -= delta_y
        clear_canvas()
        if delta_x > 0:
            character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, ax, ay)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)
    pass

def move_f_to_g():
    ax, ay, bx, by = 316, 225, 510, 92
    frame = 0
    character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
    character.clip_draw(frame * 100, 0, 100, 100, bx, by)
    delta_x = (ax - bx) // 10
    delta_y = (ay - by) // 10
    while (ax <= bx):
        ax -= delta_x
        ay -= delta_y
        clear_canvas()
        if delta_x > 0:
            character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, ax, ay)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)
    pass

def move_g_to_h():
    ax, ay, bx, by = 510,92,692,518
    frame = 0
    character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
    character.clip_draw(frame * 100, 0, 100, 100, bx, by)
    delta_x = (ax - bx) // 10
    delta_y = (ay - by) // 10
    while (ax <= bx):
        ax -= delta_x
        ay -= delta_y
        clear_canvas()
        if delta_x > 0:
            character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, ax, ay)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)


def move_h_to_i():
    ax, ay, bx, by = 692, 518, 682, 336
    frame = 0
    character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
    character.clip_draw(frame * 100, 0, 100, 100, bx, by)
    delta_x = (ax - bx) // 10
    delta_y = (ay - by) // 10
    while (ax >= bx):
        ax -= delta_x
        ay -= delta_y
        clear_canvas()
        if delta_x > 0:
            character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, ax, ay)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)

def move_i_to_j():
    ax, ay, bx, by = 682, 336, 712, 349
    frame = 0
    character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
    character.clip_draw(frame * 100, 0, 100, 100, bx, by)
    delta_x = (ax - bx) // 10
    delta_y = (ay - by) // 10
    while (ax <= bx):
        ax -= delta_x
        ay -= delta_y
        clear_canvas()
        if delta_x > 0:
            character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, ax, ay)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)

def move_i_to_a():
    ax, ay, bx, by = 682, 336, 203, 535
    frame = 0
    character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
    character.clip_draw(frame * 100, 0, 100, 100, bx, by)
    delta_x = (ax - bx) // 10
    delta_y = (ay - by) // 10
    while (ax >= bx):
        ax -= delta_x
        ay -= delta_y
        clear_canvas()
        if delta_x > 0:
            character.clip_draw(frame * 100, 0, 100, 100, ax, ay)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, ax, ay)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)
while True:
    move_a_to_b()
    move_b_to_c()
    move_c_to_d()
    move_d_to_e()
    move_e_to_f()
    move_f_to_g()
    move_g_to_h()
    move_h_to_i()
    move_i_to_j()
    move_i_to_a()


close_canvas()
