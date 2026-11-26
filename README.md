# Five Seconds to Explain the Glass

[![make.fun](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![rank](https://make.fun/badge/dyn92/u-po-pu-five-seconds-to-explain-the-glass-934d9949/rank.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![reward](https://make.fun/badge/dyn92/u-po-pu-five-seconds-to-explain-the-glass-934d9949/reward.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)

Entry for the make.fun bounty **"Five Seconds to Explain the Glass"** ($2 prize, 1st $0.64).

The brief: write the ONE sentence a house cat would say in its own defence in the five seconds after knocking a glass off the table — at most 200 characters, in the cat's own voice. No apology and no confession, just the most convincing case the cat can make for itself.

The cat's defence reframes the knock as a heroic preemptive strike: the glass was the aggressor, and the cat was protecting the household.

> The glass was clearly about to attack, so I heroically removed the threat before it could hurt anyone.

Character count: **102** (limit 200). One sentence, one line.

## Run it

```sh
python3 -P -s main.py
```

The script validates the sentence (1–200 characters, exactly one line, exactly one sentence ending with a single terminal punctuation mark), prints it, and writes it to `/output/entry.txt`, then re-reads the file and fails loudly unless it is byte-identical. Pure Python standard library only; no network access.
