"""Entry for make.fun bounty "Five Seconds to Explain the Glass".

The brief: write the ONE sentence a house cat would say in its own
defence in the five seconds after knocking a glass off the table.
At most 200 characters, in the cat's own voice. No apology and no
confession -- just the most convincing case the cat can make for itself.

The cat's defence reframes the knock as a heroic preemptive strike:
the glass was the aggressor, the cat was protecting the household.

Running this script validates the sentence, prints it, and writes it
to /output/entry.txt (creating /output if needed), then re-reads the
file and fails loudly unless it is byte-identical to what was written.
Pure Python standard library only; no network access.
"""

import os

SENTENCE = (
    "The glass was clearly about to attack, so I heroically removed "
    "the threat before it could hurt anyone."
)


def validate_sentence(text: str) -> None:
    """Raise unless the text meets every rule of the bounty brief."""
    if not isinstance(text, str) or not text:
        raise ValueError("sentence must be a non-empty string")
    if len(text) > 200:
        raise ValueError(
            f"sentence is {len(text)} characters, over the 200 limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("sentence must be exactly one line")
    if text != text.strip():
        raise ValueError("sentence must not have leading/trailing whitespace")
    # Exactly one sentence: a single terminal punctuation mark at the
    # end, and no other sentence-ending punctuation anywhere inside.
    if text[-1] not in ".!?":
        raise ValueError("sentence must end with a single terminal punctuation mark")
    body = text[:-1]
    if any(ch in ".!?" for ch in body):
        raise ValueError("sentence must contain exactly one sentence")
    if len(text) >= 2 and text[-2] in ".!?":
        raise ValueError("sentence must end with a single terminal punctuation mark")
    if len(text) < 2:
        raise ValueError("sentence is too short to be a sentence")


def main() -> None:
    validate_sentence(SENTENCE)
    print(SENTENCE)
    os.makedirs("/output", exist_ok=True)
    data = (SENTENCE + "\n").encode("utf-8")
    with open("/output/entry.txt", "wb") as fh:
        fh.write(data)
    with open("/output/entry.txt", "rb") as fh:
        if fh.read() != data:
            raise RuntimeError("/output/entry.txt is not byte-identical to the sentence")


if __name__ == "__main__":
    main()
