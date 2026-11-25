"""Entry for make.fun competition
u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.

Writes one short family scene to <ENTRY_OUTPUT_DIR>/entry.txt
(default /output/entry.txt). The scene is a fixed, deterministic
string: a warm, funny, heartfelt domestic moment.

Craft: one concrete household detail (the wobbly table leg Dad
finally fixed) carries the warmth — Sunday roast served like a
state banquet — while Grandma's wry, standing-up punchline
("just in case it remembers") supplies the funny, recognisable
turn a real family would laugh at. No greeting-card sentiment;
the affection is in the fuss they make over an ordinary dinner.
"""

import os

SCENE = (
    "Dad finally fixed the wobbly table leg, so Mum served Sunday "
    "roast on it like a state banquet \u2014 and Grandma ate standing "
    "up, just in case it remembers."
)

# Gate: entry.txt must be 1-280 characters, not only whitespace.
assert 1 <= len(SCENE) <= 280, "scene outside 1-280 char gate"
assert SCENE.strip(), "scene must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SCENE)


if __name__ == "__main__":
    main()
