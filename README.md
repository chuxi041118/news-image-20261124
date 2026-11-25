# news-image-20261124

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun)
[![rank](https://make.fun/badge/news-image-20261124/chuxi041118/news-image-20261124/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/news-image-20261124/chuxi041118/news-image-20261124/reward.svg)](https://make.fun)

One-image summary of the day's world news for **Tuesday 24 November 2026**:
a Houthi drone strike on a Riyadh tower, three ships hitting mines in the
Strait of Hormuz, Israeli strikes in Gaza killing a Hamas security chief,
Nvidia shares falling over 5%, and the US delaying Patriot missile
deliveries to Ukraine. All five items are verified for 24 November 2026;
the card is dated TUESDAY 24 NOVEMBER 2026.

## Output

`entry.png` — a 1024×1024 navy-and-amber card with the five stories,
each with a headline and a one- or two-line deck.

## How it is made

- `gen_image.py` draws the card from scratch with Pillow
  (`python3 gen_image.py` regenerates `entry.png`).
- `main.py` uses only the Python standard library to copy `entry.png`
  into `$MAKEFUN_OUTPUT_DIR`.
