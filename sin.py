# type: ignore
import displayio
from adafruit_matrixportal.matrix import Matrix
import math
import os
import time
import random
from jediah.utils import hsv_to_hex

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

num_colors = 64
palette = displayio.Palette(num_colors+1)
palette[0] = 0
for i in range(1, 65):
    palette[i] = hsv_to_hex((int(255 * (i-1)/64), 255, 255))

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