#!/usr/bin/env python3
"""Generate the GitHub social-preview card (1280x640 PNG).

Usage:
    pip install -r scripts/requirements.txt
    python scripts/make_card.py

Writes social-preview.png to the repository root, regardless of where it's run from.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "social-preview.png"

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
    # Try common font locations across macOS, Linux, and Windows.
    if bold:
        paths = [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",          # macOS
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",       # Debian/Ubuntu
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "C:\\Windows\\Fonts\\arialbd.ttf",                            # Windows
        ]
    else:
        paths = [
            "/System/Library/Fonts/Supplemental/Arial.ttf",              # macOS
            "/System/Library/Fonts/Helvetica.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",           # Debian/Ubuntu
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "C:\\Windows\\Fonts\\arial.ttf",                             # Windows
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

img.save(OUT)
print("wrote", OUT, img.size)
