from pico2d import *

open_canvas()

grass = load_image('grass.png')

character = load_image('run_animation.png')

character1 = load_image('animation_sheet.png')

x = 0

# 여기를 채우세요.

x = 0

frame = 0

left = True

while (True):

    if (left):

        while (x < 800):
            clear_canvas()

            grass.draw(400, 30)

            character.clip_draw(frame * 100, 0, 100, 100, x, 90)

            update_canvas()

            frame = (frame + 1) % 8

            x += 5

            delay(0.001)

            get_events()

    left = False

    if (left == False):

        while (x > 0):
            clear_canvas()

            grass.draw(400, 30)

            character1.clip_draw(frame * 100, 0, 100, 100, x, 90)

            update_canvas()

            frame = (frame + 1) % 8

            x -= 5

            delay(0.001)

            get_events()

    left = True

close_canvas()