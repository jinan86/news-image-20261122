# The World Today — 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/jinan86/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/jinan86/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A newspaper front page summing up the world news of **Sunday, 22 November 2026** in one image. The program copies the finished page (`entry.png`, drawn with code at build time) to the output directory and verifies the copy byte-for-byte.

## The day's stories

| Story | What the image says | Source |
|---|---|---|
| **Lead — Gulf crisis** | Iran says it hit U.S. bases in Bahrain: Tehran claims missile and drone strikes on two U.S. Patriot radar sites; Bahrain reports a fire at a civilian plant and no casualties; tankers were also hit near the Strait of Hormuz. | Al Jazeera, IANS / ANI, Euronews |
| **COP31 in overtime** | The U.N. climate summit in Antalya risks failure as fossil fuels vanish from the draft deal. | Reuters, AP |
| **No deal on "killer robots"** | U.N. talks on lethal autonomous weapons end with no binding limits. | The Verge |
| **FBI probes database hack** | The bureau probes an apparent breach of its crime database. | BBC |
| **France protests** | Fourth weekend of cost-of-living protests; crowds march again over rising prices. | The Paris Eye |
| **Flooded Gaza** | Australia, Canada, Italy and Britain call on Israel to open aid access. | The Paris Eye |
| **Also today** | Hong Kong votes for its Election Committee; Modi opens the Nitish Setu bridge in Bihar; Myanmar shaken by a 4.1 quake. | ANI, Hindustan Times |

Stories were chosen only if they happened, or were first reported, on 22 November 2026. Two big weekend stories were deliberately left out because they belong to earlier days: the capture of "El Chapo Isidro" (operation 20 Nov, announced 21 Nov) and the Peru earthquake (20 Nov local time).

## How it works

- `entry.png` — the front page, 1024×1024 PNG, drawn with Pillow (vector shapes and text only, no photos, no network) by `build_image.py` at build time.
- `main.py` — the entrypoint (Python 3.13, standard library only). It reads `entry.png` from the repository root, writes it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), then re-reads the copy and fails hard if its SHA-256 differs from the source. No network, no clock, no randomness: every run writes identical bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Competition

- Competition: https://make.fun/bounty/news-image-20261122
- Entry: "Sum up 22 November's world news in one image"

Built by @jinan86 for the make.fun bounty — referral code 95rs49se.
