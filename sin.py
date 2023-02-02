# type: ignore
import displayio
from adafruit_matrixportal.matrix import Matrix
import math
import os
import time
import random

ani_dir="/ani"
ani_files = os.listdir( ani_dir )

# initialize display
matrix = Matrix(bit_depth=4)
display = matrix.display

# create a display group
group = displayio.Group()
display.show(group)

# set the color palette
color_black = 0x000000
color_red = 0xFF0000
color_orange = 0xf56642
color_blue = 0x0000ff
color_green = 0x00ff00

def HSV_2_RGB(HSV):
    ''' Converts an integer HSV tuple (value range from 0 to 255) to an RGB tuple '''

    # Unpack the HSV tuple for readability
    H, S, V = HSV

    # Check if the color is Grayscale
    if S == 0:
        R = V
        G = V
        B = V
        return (R, G, B)

    # Make hue 0-5
    region = H // 43;

    # Find remainder part, make it from 0-255
    remainder = (H - (region * 43)) * 6; 

    # Calculate temp vars, doing integer multiplication
    P = (V * (255 - S)) >> 8;
    Q = (V * (255 - ((S * remainder) >> 8))) >> 8;
    T = (V * (255 - ((S * (255 - remainder)) >> 8))) >> 8;


    # Assign temp vars based on color cone region
    if region == 0:
        R = V
        G = T
        B = P

    elif region == 1:
        R = Q; 
        G = V; 
        B = P;

    elif region == 2:
        R = P; 
        G = V; 
        B = T;

    elif region == 3:
        R = P; 
        G = Q; 
        B = V;

    elif region == 4:
        R = T; 
        G = P; 
        B = V;

    else: 
        R = V; 
        G = P; 
        B = Q;

    rgb = 0x010000 * R + 0x000100 * G + 0x000001 * B
    return rgb

num_colors = 64
palette = displayio.Palette(num_colors+1)
palette[0] = 0
for i in range(1, 65):
    palette[i] = HSV_2_RGB((int(255 * (i-1)/64), 255, 255))


count = 0
theta = 0.02
a = 4
while True:
    count += 1
    theta += 0.2
    bitmap = displayio.Bitmap(64, 32, num_colors)
    # a_delta = a * (random.random() * 0.1) * random.randint(-1, 1)
    # a = min(10, max(2, a + a_delta))
    for x in range(64):
        y = int(a*math.sin(x + theta))
        bitmap[x, 16 + y] = 1 + int(x - 1 - count / 2.5) % (num_colors - 1)

    # create a bitmap to draw on
    group.append(displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0))

    # draw a circle
    display.refresh(target_frames_per_second=10)
    group.pop()