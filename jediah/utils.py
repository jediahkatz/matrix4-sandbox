def hsv_to_hex(hsv):
    rgb = hsv_to_rgb(hsv)
    hex = rgb_to_hex(rgb)
    return hex

def rgb_to_hex(rgb):
    r, g, b = rgb
    rgb = 0x010000 * r + 0x000100 * g + 0x000001 * b
    return int(rgb)

def hsv_to_rgb(hsv):
    h, s, v = hsv
    h = h / 360.0
    # https://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)