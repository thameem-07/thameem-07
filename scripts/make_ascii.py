from pathlib import Path
from PIL import Image

INPUT = Path("assets/source-photo.jpg")
OUTPUT = Path("assets/ascii-portrait.svg")

# ASCII characters from dark to light
CHARS = "@%#*+=-:. "

WIDTH = 70
CHAR_ASPECT = 0.50

FONT_SIZE = 10
LINE_HEIGHT = 11

TEXT_COLOR = "#c9d1d9"


def brightness_to_char(value):
    index = int(value / 256 * len(CHARS))

    if index >= len(CHARS):
        index = len(CHARS) - 1

    return CHARS[index]


def main():

    if not INPUT.exists():
        raise FileNotFoundError(
            f"Photo not found: {INPUT}"
        )

    image = Image.open(INPUT).convert("L")

    original_width, original_height = image.size

    height = int(
        original_height
        / original_width
        * WIDTH
        * CHAR_ASPECT
    )

    image = image.resize(
        (WIDTH, height)
    )

    lines = []

    for y in range(height):

        line = ""

        for x in range(WIDTH):

            brightness = image.getpixel(
                (x, y)
            )

            line += brightness_to_char(
                brightness
            )

        lines.append(line.rstrip())

    svg_width = WIDTH * FONT_SIZE * 0.6
    svg_height = height * LINE_HEIGHT + 20

    svg = []

    svg.append(
        f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{svg_width}"
height="{svg_height}"
viewBox="0 0 {svg_width} {svg_height}">

<style>

.ascii {{
    font-family: monospace;
    font-size: {FONT_SIZE}px;
    fill: {TEXT_COLOR};
}}

.row {{
    opacity: 0;
    animation: reveal 0.45s ease-out forwards;
}}

@keyframes reveal {{

    from {{
        opacity: 0;
        transform: translateX(-10px);
    }}

    to {{
        opacity: 1;
        transform: translateX(0);
    }}

}}

</style>
'''
    )

    for row, line in enumerate(lines):

        # Escape XML-sensitive characters
        line = (
            line
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

        delay = row * 0.035

        y = 15 + row * LINE_HEIGHT

        svg.append(
            f'''<text
x="0"
y="{y}"
class="ascii row"
style="animation-delay:{delay:.3f}s"
>{line}</text>'''
        )

    svg.append("</svg>")

    OUTPUT.write_text(
        "\n".join(svg),
        encoding="utf-8"
    )

    print()
    print("ASCII portrait created!")
    print(f"Saved to: {OUTPUT}")
    print(f"Size: {WIDTH} columns × {height} rows")


if __name__ == "__main__":
    main()
