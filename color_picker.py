import displayio
from adafruit_matrixportal.matrix import Matrix

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

from adafruit_airlift.esp32 import ESP32

import time

esp32 = ESP32()

adapter = esp32.start_bluetooth()

ble = BLERadio(adapter)
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

# initialize display
matrix = Matrix(bit_depth=6)
display = matrix.display

# create a display group
group = displayio.Group()
display.show(group)

palette = displayio.Palette(1)
bitmap = displayio.Bitmap(64, 32, 1)
bitmap.fill(0)

grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0)
group.append(grid)

while True:
    ble.start_advertising(advertisement)
    print("waiting to connect")
    while not ble.connected:
        pass
    print("connected: trying to read input")
    current_color = 0x0
    new_color = 0x0
    while ble.connected:
        # Returns b'' if nothing was read.
        color_bytes = uart.read(5)
        if color_bytes and color_bytes.startswith('!C'):
            print(color_bytes, color_bytes[2:], len(color_bytes))
            palette[0] = color_bytes[2:]

        if new_color != current_color:
            grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0)
            group.pop()
            group.append(grid)


            