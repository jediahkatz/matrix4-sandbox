# type: ignore
import displayio
from adafruit_matrixportal.matrix import Matrix
import os
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

# # set the color palette
color_black = 0x000000
color_red = 0xFF0000
color_orange = 0xf56642
color_blue = 0x0000ff
color_green = 0x00ff00

palette_colors = [
    0x0,
    hsv_to_hex((265, 1, 1)),
    0x0,
    hsv_to_hex((135, 1, 1)),
    0x0,
    hsv_to_hex((28, 1, 1)),
]
print(palette_colors)
num_colors = len(palette_colors)

# num_colors = 8 
palette = displayio.Palette(num_colors)
for i in range(num_colors):
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
i = 0
while True:
    i += 1
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

        # Causes blinking
        # palette[1] = hsv_to_hex((5 * i % 360, 1, 1))
        # palette[3] = hsv_to_hex((20 * i % 360, 1, 1))
        # palette[3] = hsv_to_hex((20 * i % 360, 1, 1))

        # create a bitmap to draw on
        group.append(displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0))

        # draw a circle
        display.refresh(target_frames_per_second=10)
        group.pop()