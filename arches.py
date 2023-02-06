# type: ignore
import displayio
from adafruit_matrixportal.matrix import Matrix
import math
import time
from jediah.utils import hsv_to_hex

# initialize display
matrix = Matrix(bit_depth=2)
display = matrix.display
# display.auto_refresh = True

# create a display group
group = displayio.Group()
display.show(group)

# set the color palette
num_colors = 64
palette = displayio.Palette(num_colors*1+1)
for p in range(1):
    palette[num_colors] = 0
    for i in range(64):
        palette[i] = hsv_to_hex((int(360 * i/64), 1, 1))

bitmap = displayio.Bitmap(64, 32, num_colors+1)
bitmap.fill(num_colors)

def draw_arches(bitmap, num_rows=4, branching_coef=4, pan=0):
    step = math.ceil((32-2) / (num_rows))
    if (step + 1) * (num_rows - 1) > 32:
        step = math.floor((32-2) / (num_rows))
    start = (32 - (num_rows-1)*step - 1) // 2
    print(step, 32 - (num_rows-1)*step)
    for y0 in range(start, 32, step):
        for x in range(0, 64, 1):
            for y in range(y0, y0 + 1):
                print(x, y)
                bitmap[x, y] = int(y0 * branching_coef * x + x + pan) % num_colors

grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0)

while True:
    # draw a circle
    for num_rows in range(2, 16):
        num_rows_until_zoom = 8
        iter_start = 5 if num_rows < num_rows_until_zoom else 0
        iter_depth = 10
        iter_end = 0 if num_rows == num_rows_until_zoom-1 else iter_start
        for i in list(range(iter_depth, iter_start, -1)) + list(range(iter_start, iter_depth+1)):
            bitmap.fill(num_colors)
            draw_arches(bitmap, num_rows=num_rows, branching_coef=8/math.pow(2, i), pan=0)
            grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0)
            group.append(grid)
            if len(group) > 1:
                group.pop(0)
            time.sleep(0.1)
    # display.refresh()
    # time.sleep(3)