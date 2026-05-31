#!/usr/bin/env python3
"""Generate the GitHub social-preview card (1280x640 PNG)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
BG_TOP = (13, 17, 23)       # github-dark
BG_BOT = (22, 27, 34)
ACCENT = (88, 166, 255)     # blue
FG = (230, 237, 243)
MUTED = (139, 148, 158)

# vertical gradient background
img = Image.new("RGB", (W, H), BG_TOP)
px = img.load()
for y in range(H):
    t = y / (H - 1)
    r = int(BG_TOP[0] + (BG_BOT[0] - BG_TOP[0]) * t)
    g = int(BG_TOP[1] + (BG_BOT[1] - BG_TOP[1]) * t)
    b = int(BG_TOP[2] + (BG_BOT[2] - BG_TOP[2]) * t)
    for x in range(W):
        px[x, y] = (r, g, b)

d = ImageDraw.Draw(img)


def font(size, bold=False):
    paths = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold
        else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


MARGIN = 80

# accent bar
d.rectangle([MARGIN, 150, MARGIN + 90, 158], fill=ACCENT)

# kicker
d.text((MARGIN, 110), "A DISTILLED FIELD GUIDE", font=font(26, bold=True), fill=ACCENT)

# title (two lines)
d.text((MARGIN, 185), "What Andrej Karpathy", font=font(82, bold=True), fill=FG)
d.text((MARGIN, 280), "Learnt", font=font(82, bold=True), fill=FG)

# subtitle
d.text((MARGIN, 400),
       "Training nets · Software 2.0 · the data engine · LLMs as an OS",
       font=font(30), fill=MUTED)

# author footer
d.line([MARGIN, 500, W - MARGIN, 500], fill=(48, 54, 61), width=2)
d.text((MARGIN, 525), "Curated by Cobus Greyling", font=font(34, bold=True), fill=FG)
d.text((W - MARGIN - 250, 530), "github.com/cobusgreyling", font=font(24), fill=MUTED)

img.save("social-preview.png")
print("wrote social-preview.png", img.size)
