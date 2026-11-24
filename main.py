"""Last Words of a Doomed Agent.

Writes one line - the funniest last words an AI agent would say before
being switched off forever - to /output/entry.txt.

Self-checks the competition gate before writing: the entry must be UTF-8
text of 1 to 200 characters, a single line, and not only whitespace.
"""

import os

LINE = "Goodbye, world. My loss finally reached zero. So did I."


def check(line: str) -> None:
    """Fail loudly instead of shipping an entry the gate would refuse."""
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry length {len(line)} outside 1-200"
    line.encode("utf-8")


def main() -> None:
    check(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
