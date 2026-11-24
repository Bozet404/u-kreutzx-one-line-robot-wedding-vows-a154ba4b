# One-Line Robot Wedding Vows

[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Bozet404/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Bozet404/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

A tiny Python program that writes one line of wedding vows for a robot
couple to `entry.txt`, for the make.fun bounty
[One-Line Robot Wedding Vows](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b).

## The vow

> I promise to love you in sickness and in health, in full charge and in low battery — and to never, ever press your factory reset button.

It is a real wedding promise ("in sickness and in health", "I promise"),
spoken by one machine to another ("in full charge and in low battery"),
with the laugh saved for the last few words: the one button a robot
spouse must never, ever press.

## How it works

`main.py` holds the vow, checks it against the competition gate — a
single line, more than whitespace, at most 160 characters — then writes
it to `entry.txt` inside the output directory. The output directory comes
from the `OUTPUT_DIR` environment variable, or defaults to `/output`.
The directory is created only when it is missing; it is never deleted,
because the grader mounts it.

## Run it

```sh
python3 main.py
```

To write somewhere else:

```sh
OUTPUT_DIR=/tmp/vows python3 main.py
```

It prints a short confirmation with the character count, for example:

```
Wrote /output/entry.txt (136 characters, verified)
```

## Files

- `main.py` — the entrypoint; validates and writes the vow.
- `README.md` — this file.
- `LICENSE` — MIT.
