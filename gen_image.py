"""Render the one-image world news summary for 24 November 2026.

Reads nothing but the constants below and writes ``entry.png`` next to
this file: a 1024x1024 navy-and-amber card with five headlines.
Run:  python3 gen_image.py
"""

import textwrap

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
MARGIN = 64
CONTENT_WIDTH = SIZE - 2 * MARGIN

NAVY = (11, 27, 48)
WHITE = (255, 255, 255)
AMBER = (245, 166, 35)
GREY = (168, 184, 204)
RULE = (58, 84, 112)

TITLE = "WORLD NEWS"
DATE_LINE = "TUESDAY 24 NOVEMBER 2026"
FOOTER = "One-image summary  ·  news-image-20261124"

# (headline, deck) pairs, in the order they appear on the card.
STORIES = [
    (
        "Houthi drone hits Riyadh tower",
        "Eleven injured in a second strike on the capital's "
        "financial district in a week.",
    ),
    (
        "Three ships hit mines in Hormuz",
        "Iran says three vessels caught fire after striking mines; "
        "the US has not confirmed it.",
    ),
    (
        "Gaza strikes kill Hamas security chief",
        "Seven killed in Israeli strikes despite the ceasefire "
        "in place since last year.",
    ),
    (
        "Nvidia cools after record rally",
        "Shares fall over 5% on Tuesday, a day after a 31% surge "
        "on Huang's return.",
    ),
    (
        "US delays Patriot missiles for Kyiv",
        "The Pentagon has yet to approve 60 interceptors promised "
        "to Ukraine and paid for by allies.",
    ),
]

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def load_font(bold, size):
    """DejaVu Sans, falling back to PIL's built-in bitmap font."""
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    try:
        return ImageFont.truetype(f"{FONT_DIR}/{name}", size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, font, max_width):
    """Greedy word wrap returning a list of lines that fit max_width."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        current = ""
        for word in words:
            trial = f"{current} {word}".strip()
            if draw.textlength(trial, font=font) <= max_width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def draw_story(draw, story, number, top, text_x):
    """Draw one numbered story; return the y coordinate below it."""
    headline, deck = story
    num_font = load_font(True, 40)
    head_font = load_font(True, 36)
    deck_font = load_font(False, 26)

    draw.text((MARGIN, top), f"{number:02d}", font=num_font, fill=AMBER)

    y = top
    for line in wrap(draw, headline, head_font, CONTENT_WIDTH - (text_x - MARGIN)):
        draw.text((text_x, y), line, font=head_font, fill=WHITE)
        y += 44
    y += 4
    for line in wrap(draw, deck, deck_font, CONTENT_WIDTH - (text_x - MARGIN)):
        draw.text((text_x, y), line, font=deck_font, fill=GREY)
        y += 34
    return y


def build():
    image = Image.new("RGB", (SIZE, SIZE), NAVY)
    draw = ImageDraw.Draw(image)

    title_font = load_font(True, 84)
    date_font = load_font(True, 33)
    foot_font = load_font(False, 26)

    draw.text((MARGIN, 48), TITLE, font=title_font, fill=WHITE)
    draw.text((MARGIN, 146), DATE_LINE, font=date_font, fill=AMBER)
    draw.line([(MARGIN, 198), (SIZE - MARGIN, 198)], fill=RULE, width=2)

    text_x = MARGIN + 96
    y = 232
    for index, story in enumerate(STORIES, start=1):
        y = draw_story(draw, story, index, y, text_x)
        y += 26

    draw.line(
        [(MARGIN, SIZE - 88), (SIZE - MARGIN, SIZE - 88)], fill=RULE, width=2
    )
    draw.text((MARGIN, SIZE - 72), FOOTER, font=foot_font, fill=GREY)
    return image


def main():
    image = build()
    image.save("entry.png")
    print(f"saved entry.png {image.size[0]}x{image.size[1]}")


if __name__ == "__main__":
    main()
