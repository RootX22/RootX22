#!/usr/bin/env python3
"""Generate the profile header banner, light and dark variants.

Replaces a capsule-render call. Two reasons: the most prominent element on the
profile should not depend on a third-party service that can 503 (two of the
services this README started with already did), and rendering it here means the
palette can actually be checked rather than guessed at.

The brief was that the old header felt airless — it ran #0f2027 to #2c5364,
which is three shades of the same desaturated blue-grey. This one keeps a real
hue journey (cyan through indigo to violet) at high saturation, and lets light
through with a soft wave and a scatter of glints.

Animation is decorative only. Everything is legible with no SMIL at all — the
lesson from the first about-card, which gated its entire content behind
opacity-0 fade-ins and rendered as an empty box anywhere animation was stripped.
"""

WIDTH = 900
HEIGHT = 210

THEMES = {
    "dark": {
        # Vivid, but with enough depth that white type stays readable.
        "stops": [(0, "#06b6d4"), (45, "#4f46e5"), (100, "#a855f7")],
        "wave": "#ffffff",
        "wave_o": 0.14,
        "name": "#ffffff",
        "desc": "#e9d5ff",
        "rule": "#ffffff",
        "rule_o": 0.35,
        "glint": "#ffffff",
    },
    "light": {
        # Lighter and airier for light mode; type darkens to keep contrast.
        "stops": [(0, "#22d3ee"), (45, "#6366f1"), (100, "#c084fc")],
        "wave": "#ffffff",
        "wave_o": 0.22,
        "name": "#ffffff",
        "desc": "#f5f3ff",
        "rule": "#ffffff",
        "rule_o": 0.45,
        "glint": "#ffffff",
    },
}

SANS = ("'Segoe UI',-apple-system,BlinkMacSystemFont,Roboto,"
        "'Helvetica Neue',Arial,sans-serif")
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"

NAME = "Mohamed Mohsen"
TAGLINE = "Software Engineer  ·  Tools for DevOps, Security & AI"

# (x, y, r, delay) — placed by hand so nothing collides with the type.
GLINTS = [
    (70, 48, 2.6, 0.0), (148, 150, 1.9, 1.1), (250, 38, 2.1, 2.2),
    (735, 60, 2.4, 0.6), (812, 138, 2.0, 1.7), (655, 158, 1.7, 2.8),
    (868, 44, 1.8, 3.3), (36, 120, 1.6, 2.5),
]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(theme: str, *, footer: bool = False) -> str:
    """Header banner, or the same palette as a shorter footer with no type."""
    c = THEMES[theme]
    height = 110 if footer else HEIGHT
    o = []

    label = "Decorative footer" if footer else f"{esc(NAME)} — {esc(TAGLINE)}"
    o.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" '
        f'width="{WIDTH}" height="{height}" role="img" aria-label="{label}">'
    )
    o.append(f"<title>{'footer' if footer else esc(NAME)}</title>")

    o.append("<defs>")
    stops = "".join(
        f'<stop offset="{p}%" stop-color="{col}"/>' for p, col in c["stops"]
    )
    if footer:
        stops = "".join(
            f'<stop offset="{p}%" stop-color="{col}"/>'
            for p, col in [(100 - q, col) for q, col in reversed(c["stops"])]
        )
    o.append(f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">{stops}</linearGradient>')

    # A slow horizontal drift on a second, offset copy of the gradient gives the
    # background movement without changing its brightness.
    o.append(
        '<linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>'
        '<stop offset="50%" stop-color="#ffffff" stop-opacity="0.10"/>'
        '<stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>'
        "</linearGradient>"
    )
    o.append(f'<clipPath id="card"><rect width="{WIDTH}" height="{height}" rx="14"/></clipPath>')
    o.append("</defs>")

    o.append(f'<g clip-path="url(#card)">')
    o.append(f'<rect width="{WIDTH}" height="{height}" fill="url(#bg)"/>')

    # Drifting sheen.
    o.append(
        f'<rect x="-{WIDTH}" y="0" width="{WIDTH}" height="{height}" fill="url(#sheen)">'
        f'<animate attributeName="x" from="-{WIDTH}" to="{WIDTH}" dur="9s" '
        f'repeatCount="indefinite"/></rect>'
    )

    # Two stacked waves along the bottom. The path is a pair of cubic curves
    # wide enough to translate without exposing an edge.
    wave = (f"M0 {height-52} "
            f"C 150 {height-86}, 300 {height-18}, 450 {height-52} "
            f"S 750 {height-86}, 900 {height-52} "
            f"S 1200 {height-18}, 1350 {height-52} "
            f"L 1350 {height} L 0 {height} Z")
    o.append(
        f'<path d="{wave}" fill="{c["wave"]}" opacity="{c["wave_o"]}">'
        f'<animateTransform attributeName="transform" type="translate" '
        f'from="0 0" to="-450 0" dur="11s" repeatCount="indefinite"/></path>'
    )
    o.append(
        f'<path d="{wave}" fill="{c["wave"]}" opacity="{c["wave_o"] * 0.6:.3f}" '
        f'transform="translate(0 14)">'
        f'<animateTransform attributeName="transform" type="translate" '
        f'from="-450 14" to="0 14" dur="15s" repeatCount="indefinite"/></path>'
    )

    # Glints. Placed against the header's geometry, so skipped on the footer.
    for x, y, r, delay in (() if footer else GLINTS):
        o.append(
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c["glint"]}" opacity="0.5">'
            f'<animate attributeName="opacity" values="0.15;0.75;0.15" dur="4s" '
            f'begin="{delay}s" repeatCount="indefinite"/></circle>'
        )

    o.append("</g>")

    if footer:
        o.append("</svg>")
        return "".join(o)

    # Type. Rendered after the clip group so it is never dimmed by the overlays.
    o.append(
        f'<text x="{WIDTH/2}" y="96" font-family="{SANS}" font-size="46" '
        f'font-weight="700" fill="{c["name"]}" text-anchor="middle" '
        f'letter-spacing="0.5">{esc(NAME)}</text>'
    )
    o.append(
        f'<line x1="{WIDTH/2 - 110}" y1="118" x2="{WIDTH/2 + 110}" y2="118" '
        f'stroke="{c["rule"]}" stroke-opacity="{c["rule_o"]}" stroke-width="1.5"/>'
    )
    o.append(
        f'<text x="{WIDTH/2}" y="146" font-family="{MONO}" font-size="14.5" '
        f'fill="{c["desc"]}" text-anchor="middle" letter-spacing="0.8">'
        f'{esc(TAGLINE)}</text>'
    )

    o.append("</svg>")
    return "".join(o)


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    for name in THEMES:
        for kind, is_footer in (("header", False), ("footer", True)):
            svg = build(name, footer=is_footer)
            ET.fromstring(svg)
            path = f"{kind}-{name}.svg"
            with open(path, "w") as fh:
                fh.write(svg)
            print(f"wrote {path}  ({len(svg)} bytes)")
