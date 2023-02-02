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

num_colors = 2
palette = displayio.Palette(num_colors)
palette[0] = color_black
palette[1] = 0xffffff



bitmap = displayio.Bitmap(64, 32, num_colors)
# x, y, count, color_idx
# trails = [(0, 0, 0, 1), (10, 0, 0, 1), (20, 0, 0, 1), (30, 0, 0, 1), (40, 0, 0, 1)]
trails = [
    (random.randint(0, 63), random.randint(0, 31), 0, 1) for i in range(30)
]
wind = random.randint(-2, 2)
count = 0
while True:
    count += 1
    if count % 30 == 0:
        wind = random.randint(-2, 2)
    for i, (x, y, count, color) in enumerate(trails):

        bitmap[x, y] = 0
        x = (x + wind + random.randint(-1, 1)) % 64
        y = (y + random.randint(1, 2)) % 32
        bitmap[x, y] = color
        trails[i] = (x, y, count + 1, color)

        # create a bitmap to draw on
        group.append(displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0))

        # draw a circle
        display.refresh(target_frames_per_second=60)
        group.pop()

# Circle
# bitmap = displayio.Bitmap(64, 32, 3)
    # for r2 in range(16):
    #     for x in range(32-r2, 32+r2):
    #         for y in range(16-r2, 16+r2):
    #             r = math.sqrt((32-x)*(32-x) + (16-y)*(16-y))
    #             if r < r2 and r > r2-2:
    #                 bitmap[x, y] = 1
    #             else:
    #                 bitmap[x, y] = 0