"""Cinematic grade for hero/background imagery.
Unifies the real Reene photos into one art-directed set:
filmic S-curve, cool shadows toward the brand blue, warm highlights,
slight desaturation so the UI blue stays the loudest colour on screen."""
from PIL import Image, ImageEnhance
import os

SRC = ['CTSCAN.png', 'MRI.png', 'LAB.png', 'RECEPTION.png', 'facility.png',
       'XRAY.png', 'ULTRASOUND.png', 'laboratorytest.png', 'labequipments.png', 'ECG.png']
OUT = 'images/graded'
os.makedirs(OUT, exist_ok=True)

def curve(shadow_lift, gamma, gain):
    """build a 256 LUT: lift blacks, apply gamma, then gain"""
    lut = []
    for i in range(256):
        v = i / 255.0
        v = shadow_lift + v * (1.0 - shadow_lift)      # lift blacks (filmic)
        v = pow(v, gamma)
        v = min(1.0, v * gain)
        lut.append(int(round(v * 255)))
    return lut

# per-channel: cool the shadows, keep highlights just warm
r_lut = curve(0.020, 1.03, 1.02)
g_lut = curve(0.026, 1.00, 1.00)
b_lut = curve(0.040, 0.97, 1.01)

for name in SRC:
    p = os.path.join('images', name)
    if not os.path.exists(p):
        print('skip (missing):', name); continue
    im = Image.open(p).convert('RGB')

    im = im.point(r_lut * 1 + g_lut * 1 + b_lut * 1)   # 768-entry LUT = per channel
    im = ImageEnhance.Color(im).enhance(0.86)          # pull saturation back
    im = ImageEnhance.Contrast(im).enhance(1.11)       # firm up midtones

    # cap the long edge — these are backdrops, not print
    im.thumbnail((2200, 2200), Image.LANCZOS)

    dst = os.path.join(OUT, os.path.splitext(name)[0] + '.jpg')
    im.save(dst, 'JPEG', quality=82, optimize=True, progressive=True)
    before = os.path.getsize(p) / 1048576
    after = os.path.getsize(dst) / 1048576
    print('%-20s %5.2fMB -> %4.2fMB  %s' % (name, before, after, im.size))
