# type: ignore
# animated_gif_player.py - play a BMP list like an animated gif
# Take an animated gif, convert it to a list of numbered BMP files.
# For instance, with ImageMagick you can do this with:
#   convert anim.gif -coalesce -resize 120x120 BMP:anim-%03d.bmp
# This creates a set of 120x120 BMP named "anim-000.bmp", "anim-001.bmp"
# Copy all these files to your "ani_dir" as set below, say with:
#   cp anim*bmp /Volumes/CIRCUITPY/ani
# 17 Jul 2021 - @todbot
import os
import displayio

from adafruit_matrixportal.matrix import Matrix

# directory on CIRCUITPY where BMP animation frames are stored
ani_dir="/ani"
ani_files = os.listdir( ani_dir )

matrix = Matrix()
display = matrix.display
group = displayio.Group()

display.show(group)

while True:
    for name in ani_files:
        filename = ani_dir + "/" + name
        print("playing ",filename)
        with open(filename, "rb") as f:
            odb = displayio.OnDiskBitmap(f)
            bitmap = displayio.TileGrid(odb, pixel_shader=odb.pixel_shader)
            group.append(bitmap)
            # Wait for the image to load.
            display.refresh(target_frames_per_second=20)
            group.pop() # remove bitmap so we don't run out of memory
    print("at end, going again!")
