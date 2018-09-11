from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
x = 400
y=90
left=False
right=False
up=False
down=False
count=0;
degree=0;
while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
   
    if(count<200):
        x=x+2
    elif(count<450):
        y=y+2
    elif(count<850):
        x=x-2
    elif(count<1100):
        y=y-2
    elif(count<1300):
        x=x+2
    elif(count<1375):
        degree=degree+0.1
        x=x+10*math.cos(degree)
        y=y+10*math.sin(degree)
    elif(count==1375):
        count=0
        degree=0
        x=400
        y=90
    count=count+1
    delay(0.001)
close_canvas()
