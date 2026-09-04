#!/usr/bin/env python3
"""Generate the animated "about" terminal card, in a light and a dark variant.

GitHub sanitises inline SVG in Markdown, but an SVG committed to the repo and
referenced with <img> renders fine, animations included. Two files plus a
<picture> element is how you get a theme-aware card — GitHub swaps the source
on prefers-color-scheme, which a single file with an internal media query
cannot do reliably behind their image proxy.

Design constraint that drove the structure: **the animation never gates the
content**. An earlier version faded each line in from opacity 0, which meant
anything not running SMIL — a static rasteriser, a link preview, a reader that
strips animation — showed an empty terminal window. Everything here is fully
legible at t=0; the motion (cursor blink, sweep, pulse) is decoration layered
on top.

Fonts must be generic: an SVG loaded as an image cannot fetch a webfont, so
this asks for a monospace stack and lets the platform decide.
"""

THEMES = {
    "dark": {
        "chrome":  "#161b22",
        "body":    "#0d1117",
        "border":  "#30363d",
        "prompt":  "#5ee1a0",
        "cmd":     "#e6edf3",
        "output":  "#8b949e",
        "accent":  "#36bcf7",
        "accent2": "#f2c14e",
        "title":   "#6e7681",
        "sweep":   "#36bcf7",
        "sweep_o": "0.055",
    },
    "light": {
        "chrome":  "#eaeef2",
        "body":    "#ffffff",
        "border":  "#d0d7de",
        "prompt":  "#1a7f37",
        "cmd":     "#1f2328",
        "output":  "#57606a",
        "accent":  "#0969da",
        "accent2": "#9a6700",
        "title":   "#6e7781",
        "sweep":   "#0969da",
        "sweep_o": "0.045",
    },
}

MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

# (kind, text). Column split for two-column kinds is on the double space.
LINES = [
    ("cmd",    "whoami"),
    ("out",    "software engineer — i build tools other developers run"),
    ("gap",    ""),
    ("cmd",    "ls ~/open-source"),
    ("link",   "sentinel-audit  linux hardening auditor · pure bash"),
    ("link",   "deploy-forge  zero-downtime deploys · atomic swaps"),
    ("link",   "wp-sentinel  wordpress scanner · detection-only"),
    ("link",   "tls-sentry  tls certificate monitor · zero deps"),
    ("link",   "cronscope  crontab linter + weekly heatmap"),
    ("link",   "groundcheck  rag groundedness linter · deterministic"),
    ("gap",    ""),
    ("cmd",    "cat also-shipped.txt"),
    ("bullet", "async trading engine  XAUUSD · numba · ~13.7k LOC  (private)"),
    ("bullet", "webrtc video platform  JT1078 → MediaMTX  (private)"),
    ("gap",    ""),
    ("cmd",    "echo $PHILOSOPHY"),
    ("quote",  "“small, tested, and honest about its limits”"),
]

LINE_H = 25
GAP_H = 12
TOP = 88
WIDTH = 880
COL2 = 300          # x of the second column for bullet/link rows


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, fill, size, content, weight=None, style=None, anchor=None):
    attrs = [
        f'x="{x}"', f'y="{y}"', f'font-family="{MONO}"',
        f'font-size="{size}"', f'fill="{fill}"',
    ]
    if weight:
        attrs.append(f'font-weight="{weight}"')
    if style:
        attrs.append(f'font-style="{style}"')
    if anchor:
        attrs.append(f'text-anchor="{anchor}"')
    return f'<text {" ".join(attrs)}>{esc(content)}</text>'


def build(theme_name: str) -> str:
    c = THEMES[theme_name]

    body_h = sum(GAP_H if k == "gap" else LINE_H for k, _ in LINES)
    height = TOP + body_h + 46

    o = []
    o.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" '
        f'width="{WIDTH}" height="{height}" role="img" '
        f'aria-label="Terminal card. whoami: systems engineer, real-time '
        f'infrastructure. Focus: async trading engines, WebRTC video pipelines, '
        f'multi-tenant SaaS. Open source: sentinel-audit, deploy-forge.">'
    )
    o.append("<title>about</title>")
    o.append("<defs>")
    # Sweep gradient — a soft band that travels down the card once per cycle.
    o.append(
        f'<linearGradient id="sw" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0%" stop-color="{c["sweep"]}" stop-opacity="0"/>'
        f'<stop offset="50%" stop-color="{c["sweep"]}" stop-opacity="{c["sweep_o"]}"/>'
        f'<stop offset="100%" stop-color="{c["sweep"]}" stop-opacity="0"/>'
        f"</linearGradient>"
    )
    o.append(f'<clipPath id="win"><rect y="46" width="{WIDTH}" height="{height-46}"/></clipPath>')
    o.append("</defs>")

    # ── window ──────────────────────────────────────────────────────────────
    o.append(f'<rect width="{WIDTH}" height="{height}" rx="12" fill="{c["body"]}"/>')
    o.append(
        f'<path d="M0 12a12 12 0 0 1 12-12h{WIDTH-24}a12 12 0 0 1 12 12v34H0z" '
        f'fill="{c["chrome"]}"/>'
    )

    # Decorative sweep, clipped to the body so it never crosses the title bar.
    o.append(
        f'<g clip-path="url(#win)">'
        f'<rect x="0" y="-140" width="{WIDTH}" height="140" fill="url(#sw)">'
        f'<animate attributeName="y" from="20" to="{height}" dur="7s" '
        f'repeatCount="indefinite"/></rect></g>'
    )

    o.append(
        f'<rect x="0.5" y="0.5" width="{WIDTH-1}" height="{height-1}" rx="12" '
        f'fill="none" stroke="{c["border"]}"/>'
    )
    o.append(f'<line x1="0" y1="46" x2="{WIDTH}" y2="46" stroke="{c["border"]}"/>')

    for i, col in enumerate(("#ff5f57", "#febc2e", "#28c840")):
        o.append(f'<circle cx="{22 + i*20}" cy="23" r="6" fill="{col}"/>')

    o.append(text(WIDTH / 2, 28, c["title"], 12.5, "mohamed@systems — ~", anchor="middle"))

    # ── body ────────────────────────────────────────────────────────────────
    y = TOP
    for kind, content in LINES:
        if kind == "gap":
            y += GAP_H
            continue

        if kind == "cmd":
            o.append(text(28, y, c["prompt"], 14.5, "$", weight="600"))
            o.append(text(48, y, c["cmd"], 14.5, content))

        elif kind == "out":
            o.append(text(48, y, c["accent"], 14.5, content, weight="600"))

        elif kind == "bullet":
            label, _, detail = content.partition("  ")
            o.append(text(48, y, c["accent2"], 13.5, "▸"))
            o.append(text(68, y, c["cmd"], 13.5, label))
            o.append(text(COL2, y, c["output"], 13.5, detail))

        elif kind == "link":
            name, _, detail = content.partition("  ")
            o.append(text(48, y, c["accent"], 13.5, name, weight="600"))
            o.append(text(COL2, y, c["output"], 13.5, detail))

        elif kind == "quote":
            o.append(text(48, y, c["prompt"], 13.5, content, style="italic"))

        y += LINE_H

    # ── prompt + blinking cursor ────────────────────────────────────────────
    # Visible as a solid block when animation is unavailable.
    y += 4
    o.append(text(28, y, c["prompt"], 14.5, "$", weight="600"))
    o.append(
        f'<rect x="48" y="{y-12}" width="9" height="16" fill="{c["accent"]}">'
        f'<animate attributeName="opacity" values="1;1;0;0" dur="1.06s" '
        f'repeatCount="indefinite" calcMode="discrete"/></rect>'
    )

    o.append("</svg>")
    return "".join(o)


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    for name in THEMES:
        svg = build(name)
        ET.fromstring(svg)  # fail loudly on malformed output
        path = f"about-{name}.svg"
        with open(path, "w") as fh:
            fh.write(svg)
        print(f"wrote {path}  ({len(svg)} bytes)")
