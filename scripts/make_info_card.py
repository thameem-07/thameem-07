from pathlib import Path

OUTPUT = Path("assets/info-card.svg")

NAME = "Thameem"
USERNAME = "thameem-07"
ROLE = "B.Tech IT Student"
FOCUS = "Programming & Technology"
STACK = "C • Java • Python"
TOOLS = "Git • GitHub • DaVinci Resolve"


def main():
    width = 500
    height = 360

    rows = [
        ("Name", NAME),
        ("Role", ROLE),
        ("Focus", FOCUS),
        ("Stack", STACK),
        ("Tools", TOOLS),
    ]

    svg = []

    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<style>

.panel {{
    fill: #0d1117;
    stroke: #30363d;
    stroke-width: 2;
}}

.title {{
    fill: #58a6ff;
    font-family: monospace;
    font-size: 22px;
    font-weight: bold;
}}

.prompt {{
    fill: #8b949e;
    font-family: monospace;
    font-size: 14px;
}}

.key {{
    fill: #79c0ff;
    font-family: monospace;
    font-size: 16px;
    font-weight: bold;
}}

.value {{
    fill: #c9d1d9;
    font-family: monospace;
    font-size: 16px;
}}

.row {{
    opacity: 0;
    animation: appear 0.6s ease-out forwards;
}}

@keyframes appear {{
    from {{
        opacity: 0;
        transform: translateX(-15px);
    }}

    to {{
        opacity: 1;
        transform: translateX(0);
    }}
}}

</style>

<rect
    x="2"
    y="2"
    width="{width - 4}"
    height="{height - 4}"
    rx="14"
    class="panel"
/>

<circle cx="22" cy="22" r="6" fill="#ff5f56"/>
<circle cx="42" cy="22" r="6" fill="#ffbd2e"/>
<circle cx="62" cy="22" r="6" fill="#27c93f"/>

<text x="85" y="27" class="prompt">
    {USERNAME}@github
</text>

<text x="25" y="72" class="title">
    $ neofetch
</text>

<line
    x1="25"
    y1="88"
    x2="475"
    y2="88"
    stroke="#30363d"
/>
''')

    y = 125

    for index, (key, value) in enumerate(rows):

        delay = 0.2 + index * 0.15

        svg.append(f'''
<g
    class="row"
    style="animation-delay: {delay:.2f}s"
>

<text x="25" y="{y}" class="key">
    {key}:
</text>

<text x="145" y="{y}" class="value">
    {value}
</text>

</g>
''')

        y += 40

    svg.append(f'''
<text
    x="25"
    y="330"
    class="prompt"
>
    "Building. Learning. Experimenting."
</text>

</svg>
''')

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT.write_text(
        "\n".join(svg),
        encoding="utf-8"
    )

    print(f"Created: {OUTPUT}")


if __name__ == "__main__":
    main()
