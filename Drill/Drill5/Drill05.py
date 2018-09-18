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
    pass

def move_f_to_g():
    pass

def move_g_to_h():
    pass

def move_h_to_i():
    pass

def move_i_to_j():
    pass
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

close_canvas()
