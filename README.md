# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/competitions/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/kimbaex07/houseplant-ooo/rank.svg)](https://make.fun/competitions/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/kimbaex07/houseplant-ooo/reward.svg)](https://make.fun/competitions/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

An entry for [The Houseplant Out-of-Office](https://make.fun/competitions/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047) on make.fun.

## The entry

> Out of office. Ignored since March and thriving on spite and sunlight. Your email is now compost. Water me. Or don't.

117 characters — one line, inside the 120-character gate.

## Why it fits the judge brief

- **Plant voice:** it reads as a genuine out-of-office auto-reply, sent by the plant itself — not a human joking about a plant.
- **The plant's life drives the joke:** ignored since March, sunlight, and compost are the plant's actual biography, not decoration. The email doesn't get a polite "I'll reply when I'm back" — it gets composted.
- **Surprise and punch:** "thriving on spite" flips the expected neglected-plant pity into defiance, and the ending — "Water me. Or don't." — lands the shrug of a plant that has stopped caring.
- **Original:** no "I'll get back to you soon", no "limited access to email" — the reply the plant would actually send is indifference, not an apology.

## The joke, unpacked

The setup promises a neglected plant; the twist is that neglect made it stronger. Spite is the fertilizer. The email — the one thing the sender cares about — is already compost, which is both the plant's revenge and, literally, what plants do with dead matter. The closer hands the power back to the reader ("Water me. Or don't.") and then takes it away again: either way, the plant is fine.

## How it works

`main.py` (pure Python stdlib) reads `entry.txt`, drops a single trailing newline an editor may add (so the graded line is exact), validates it — 1–120 characters, not only whitespace, a single line — then writes the exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

This writes the entry line to `output/entry.txt`.
