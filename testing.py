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

# # set the color palette
# color_black = 0x000000
# color_red = 0xFF0000
# color_orange = 0xf56642
# color_blue = 0x0000ff
# color_green = 0x00ff00

palette_colors = [
    0x0,
    
]

num_colors = len(palette_colors)
palette = displayio.Palette(num_colors)
for i in range(len(num_colors)):
    palette[i] = palette_colors[i]

# palette[0] = color_black
# palette[1] = color_red
# palette[2] = color_black
# palette[3] = color_orange
# palette[4] = color_black
# palette[5] = color_blue
# palette[6] = color_black
# palette[7] = color_green



bitmap = displayio.Bitmap(64, 32, num_colors)
# x, y, count, color_idx
trails = [(0, 0, 0, 1)]
while True:
    (_, _, count, _) = trails[0]
    (_, _, count, color) = trails[-1]
    if count % 30 == 0:
        print(color)
        trails.append((0, 0, 0, (color + 1) % num_colors))
    if count == 90:
        trails.pop(0)
    for i, (x, y, count, color) in enumerate(trails):

        # bitmap[x, y] = 0
        x = (x + random.randint(1, 7)) % 64
        y = (y + random.randint(1, 5)) % 32
        bitmap[x, y] = color
        trails[i] = (x, y, count + 1, color)

        # create a bitmap to draw on
        group.append(displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0))

        # draw a circle
        display.refresh(target_frames_per_second=10)
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