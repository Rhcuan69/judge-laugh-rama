"""Write one office-life joke to /output/entry.txt.

Pure standard library only, no network. Deterministic: the same
bytes on every run.
"""

import os

# One concrete, true office observation with the turn in the last
# words: the protest against reply-all becomes another reply-all.
JOKE = (
    "I hit reply-all to ask everyone to stop hitting reply-all, "
    "and now forty-two colleagues agree with me."
)


def clean_line(text):
    """Collapse to a single tight line: no newlines, no extra spaces."""
    return " ".join(text.split())


def write_entry(path, text):
    line = clean_line(text)
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"), JOKE)


if __name__ == "__main__":
    main()
