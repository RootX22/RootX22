#!/usr/bin/env python3
"""Generate the profile artwork.

One source, two themes. Everything is drawn here rather than pulled from a badge
service, so the page owns its own look, loads without third-party requests, and
cannot quietly break when somebody else's widget goes down.

The visual idea is an instrument panel. The work these repositories do is
showing what a system is actually doing when it will not tell you directly, so
the page is built out of the vocabulary of measurement: a calibration grid, a
trace against a baseline, tick marks, and readouts set in monospace.

Run: python3 assets/build.py
"""

from __future__ import annotations

import pathlib

SANS = "ui-sans-serif, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"

THEMES = {
    "dark": {
        "bg0": "#0B0F14", "bg1": "#111922", "panel": "#FFFFFF", "panel_op": "0.025",
        "ink": "#EAF1F8", "muted": "#93A6B8", "faint": "#55697D",
        "grid": "#FFFFFF", "grid_op": "0.045", "edge": "#FFFFFF", "edge_op": "0.08",
        "accent": "#F0B429", "glow_op": "0.16",
    },
    "light": {
        "bg0": "#FFFFFF", "bg1": "#F3F6FA", "panel": "#0B0F14", "panel_op": "0.022",
        "ink": "#0B0F14", "muted": "#4A5B6E", "faint": "#8496A8",
        "grid": "#0B0F14", "grid_op": "0.05", "edge": "#0B0F14", "edge_op": "0.10",
        "accent": "#9A6300", "glow_op": "0.10",
    },
}


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, content, *, fill, size=14, family=SANS, weight="400", anchor="start",
         spacing=None, opacity=None):
    extra = f' letter-spacing="{spacing}"' if spacing is not None else ""
    extra += f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-family="{family}" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}"'
            f'{extra}>{esc(content)}</text>')


def grid(width, height, t, *, step=50, inset=0):
    lines = []
    x = inset + step
    while x < width - inset:
        lines.append(f'<line x1="{x}" y1="{inset}" x2="{x}" y2="{height - inset}"/>')
        x += step
    y = inset + step
    while y < height - inset:
        lines.append(f'<line x1="{inset}" y1="{y}" x2="{width - inset}" y2="{y}"/>')
        y += step
    return (f'<g stroke="{t["grid"]}" stroke-opacity="{t["grid_op"]}" stroke-width="1">'
            + "".join(lines) + "</g>")


def frame(width, height, t, *, radius=18):
    return (
        f'<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0%" stop-color="{t["bg0"]}"/>'
        f'<stop offset="100%" stop-color="{t["bg1"]}"/></linearGradient>'
        f'<clipPath id="clip"><rect width="{width}" height="{height}" rx="{radius}"/>'
        f'</clipPath>'
        f'<filter id="glow" x="-80%" y="-80%" width="260%" height="260%">'
        f'<feGaussianBlur stdDeviation="4" result="b"/>'
        f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>'
        f'</filter></defs>'
        f'<rect width="{width}" height="{height}" rx="{radius}" fill="url(#bg)"/>'
    )


def open_svg(width, height, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
            f'role="img" aria-label="{esc(label)}"><title>{esc(label)}</title>')


# -- header -------------------------------------------------------------------

TRACE = ("M616 143 L640 139 L664 145 L688 140 L712 144 L736 138 L760 142 "
         "L782 134 L798 97 L810 152 L822 128 L846 141 L870 138 L894 143 L918 140")


def header(t: dict) -> str:
    width, height = 1000, 250
    out = [open_svg(width, height, "Mohamed Mohsen, infrastructure and security engineer"),
           frame(width, height, t), '<g clip-path="url(#clip)">', grid(width, height, t)]

    # A faint wash behind the readout so the panel reads as lit. A radial falloff
    # rather than a blurred disc: no visible edge, and nothing for the renderer
    # to rasterise.
    out.append(f'<defs><radialGradient id="wash" cx="50%" cy="50%" r="50%">'
               f'<stop offset="0%" stop-color="{t["accent"]}" '
               f'stop-opacity="{t["glow_op"]}"/>'
               f'<stop offset="100%" stop-color="{t["accent"]}" stop-opacity="0"/>'
               f'</radialGradient></defs>'
               f'<circle cx="766" cy="125" r="240" fill="url(#wash)"/>')

    out.append(text(64, 72, "INFRASTRUCTURE  ·  SECURITY  ·  RELIABILITY",
                    fill=t["faint"], size=11, family=MONO, spacing="3.4"))
    out.append(text(64, 126, "Mohamed Mohsen", fill=t["ink"], size=46, weight="700",
                    spacing="-0.8"))
    out.append(f'<rect x="64" y="146" width="92" height="2" fill="{t["accent"]}"/>')
    out.append(text(64, 184, "Tools that show what your systems are actually doing.",
                    fill=t["muted"], size=15.5))

    marks = ["zero dependencies", "tested in CI", "honest about limits"]
    x = 64
    for index, mark in enumerate(marks):
        if index:
            out.append(f'<circle cx="{x - 11}" cy="{216 - 4}" r="2" '
                       f'fill="{t["accent"]}"/>')
        out.append(text(x, 216, mark, fill=t["faint"], size=11.5, family=MONO))
        x += len(mark) * 7.0 + 26

    # The readout: a measured signal against its baseline, with the one place
    # they disagree called out. That is the job these tools do, drawn once.
    out.append(f'<g><rect x="596" y="54" width="340" height="142" rx="10" '
               f'fill="{t["panel"]}" fill-opacity="{t["panel_op"]}" '
               f'stroke="{t["edge"]}" stroke-opacity="{t["edge_op"]}"/>')
    inner = []
    for i in range(1, 6):
        gx = 596 + i * (340 / 6)
        inner.append(f'<line x1="{gx:.1f}" y1="54" x2="{gx:.1f}" y2="196"/>')
    for i in range(1, 4):
        gy = 54 + i * (142 / 4)
        inner.append(f'<line x1="596" y1="{gy:.1f}" x2="936" y2="{gy:.1f}"/>')
    out.append(f'<g stroke="{t["grid"]}" stroke-opacity="{t["grid_op"]}">'
               + "".join(inner) + "</g>")

    for cx, cy, dx, dy in ((604, 62, 1, 1), (928, 62, -1, 1),
                           (604, 188, 1, -1), (928, 188, -1, -1)):
        out.append(f'<path d="M{cx} {cy + 10 * dy} L{cx} {cy} L{cx + 10 * dx} {cy}" '
                   f'fill="none" stroke="{t["accent"]}" stroke-width="1.5" '
                   f'opacity="0.55"/>')

    out.append(f'<line x1="616" y1="143" x2="918" y2="143" stroke="{t["faint"]}" '
               f'stroke-width="1" stroke-dasharray="3 5" opacity="0.7"/>')
    out.append(text(616, 160, "baseline", fill=t["faint"], size=9, family=MONO,
                    spacing="1.2"))

    out.append(f'<path id="trace" d="{TRACE}" fill="none" stroke="{t["accent"]}" '
               f'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" '
               f'stroke-dasharray="420" stroke-dashoffset="420">'
               f'<animate attributeName="stroke-dashoffset" from="420" to="0" '
               f'dur="3.6s" repeatCount="indefinite"/></path>')

    out.append(f'<circle r="3.4" fill="{t["accent"]}" filter="url(#glow)">'
               f'<animateMotion dur="3.6s" repeatCount="indefinite" rotate="0">'
               f'<mpath href="#trace" xlink:href="#trace"/></animateMotion></circle>')

    out.append(f'<path d="M782 86 L782 78 L814 78 L814 86" fill="none" '
               f'stroke="{t["muted"]}" stroke-width="1" opacity="0.8"/>')
    out.append(text(798, 70, "deviation", fill=t["muted"], size=9.5, family=MONO,
                    anchor="middle", spacing="1"))
    out.append("</g></g></svg>")
    return "".join(out)


# -- capabilities -------------------------------------------------------------

COLUMNS = (
    ("LANGUAGES", ("Python", "Bash", "PHP  ·  Laravel", "C++", "Dart  ·  Flutter")),
    ("INFRASTRUCTURE", ("Linux", "Docker", "Nginx", "AWS", "GitHub Actions")),
    ("SECURITY", ("Nmap", "Wireshark", "Burp Suite", "Metasploit", "Kali Linux")),
)


def capabilities(t: dict) -> str:
    width, height = 1000, 244
    out = [open_svg(width, height, "Capabilities"), frame(width, height, t),
           '<g clip-path="url(#clip)">', grid(width, height, t, step=50)]

    for index, (title, rows) in enumerate(COLUMNS):
        x = 64 + index * 312
        out.append(text(x, 58, title, fill=t["accent"], size=11, family=MONO,
                        weight="700", spacing="2.8"))
        out.append(f'<rect x="{x}" y="70" width="248" height="1" fill="{t["edge"]}" '
                   f'fill-opacity="{t["edge_op"]}"/>')
        for row_index, row in enumerate(rows):
            y = 100 + row_index * 27
            out.append(f'<rect x="{x}" y="{y - 8}" width="3" height="3" '
                       f'fill="{t["faint"]}"/>')
            out.append(text(x + 16, y, row, fill=t["ink"], size=13.5, family=MONO))

    out.append(f'<rect x="64" y="206" width="872" height="1" fill="{t["edge"]}" '
               f'fill-opacity="{t["edge_op"]}"/>')
    out.append(text(64, 228,
                    "Server administration end to end: provisioning, deployment, "
                    "hardening, and keeping boxes locked down.",
                    fill=t["muted"], size=12.5))
    out.append("</g></svg>")
    return "".join(out)


# -- pipeline -----------------------------------------------------------------

STAGES = (
    (40, "DataIngestionStream", "TickFeed (ABC)"),
    (255, "DualLayerEngine", "SMCStateEngine"),
    (470, "RiskExecutionManager", "sizing  ·  veto"),
    (685, "OrderRouter", "paper by default"),
)
EDGES = (("ticks", 197), ("context", 412), ("orders", 627))


def pipeline(t: dict) -> str:
    width, height = 900, 300
    out = [open_svg(width, height, "Gold Engine tick pipeline"),
           frame(width, height, t), '<g clip-path="url(#clip)">',
           grid(width, height, t, step=50)]

    out.append(text(40, 46, "TICK PIPELINE", fill=t["accent"], size=11, family=MONO,
                    weight="700", spacing="2.8"))

    for x, name, note in STAGES:
        out.append(f'<rect x="{x}" y="74" width="175" height="60" rx="8" '
                   f'fill="{t["panel"]}" fill-opacity="{t["panel_op"]}" '
                   f'stroke="{t["edge"]}" stroke-opacity="{t["edge_op"]}"/>')
        out.append(f'<rect x="{x}" y="74" width="3" height="60" fill="{t["accent"]}" '
                   f'opacity="0.75"/>')
        out.append(text(x + 88, 104, name, fill=t["ink"], size=12.5, family=MONO,
                        anchor="middle"))
        out.append(text(x + 88, 122, note, fill=t["faint"], size=10.5, family=MONO,
                        anchor="middle"))

    for index, (label, x) in enumerate(EDGES):
        out.append(f'<line x1="{x}" y1="104" x2="{x + 46}" y2="104" '
                   f'stroke="{t["muted"]}" stroke-width="1.2" opacity="0.8"/>')
        out.append(f'<path d="M{x + 46} 104 L{x + 40} 100.5 L{x + 40} 107.5 Z" '
                   f'fill="{t["muted"]}" opacity="0.8"/>')
        out.append(text(x + 23, 94, label, fill=t["faint"], size=9.5, family=MONO,
                        anchor="middle"))
        # A packet travelling the edge, so the diagram reads as a flow.
        out.append(f'<circle cy="104" r="2.6" fill="{t["accent"]}">'
                   f'<animate attributeName="cx" from="{x}" to="{x + 44}" dur="1.4s" '
                   f'begin="{index * 0.45}s" repeatCount="indefinite"/>'
                   f'<animate attributeName="opacity" values="0;1;1;0" dur="1.4s" '
                   f'begin="{index * 0.45}s" repeatCount="indefinite"/></circle>')

    out.append(f'<path d="M342 134 L342 160 L200 160 M342 160 L500 160" fill="none" '
               f'stroke="{t["edge"]}" stroke-opacity="{t["edge_op"]}" '
               f'stroke-width="1.2"/>')
    out.append(f'<rect x="108" y="176" width="292" height="50" rx="8" '
               f'fill="{t["panel"]}" fill-opacity="{t["panel_op"]}" '
               f'stroke="{t["edge"]}" stroke-opacity="{t["edge_op"]}"/>')
    out.append(text(124, 198, "static layer", fill=t["ink"], size=11.5, family=MONO))
    out.append(text(124, 215, "on candle close: pools, order blocks, bias",
                    fill=t["faint"], size=10, family=MONO))
    out.append(f'<rect x="424" y="176" width="292" height="50" rx="8" '
               f'fill="{t["panel"]}" fill-opacity="{t["panel_op"]}" '
               f'stroke="{t["edge"]}" stroke-opacity="{t["edge_op"]}"/>')
    out.append(text(440, 198, "dynamic layer", fill=t["ink"], size=11.5, family=MONO))
    out.append(text(440, 215, "every tick, O(1): sweep, mitigation FSM",
                    fill=t["faint"], size=10, family=MONO))

    out.append(f'<rect x="40" y="252" width="820" height="1" fill="{t["edge"]}" '
               f'fill-opacity="{t["edge_op"]}"/>')
    out.append(text(40, 274,
                    "Heavy structural work only on candle close; constant work per "
                    "tick. Risk sits before the router, and the router is paper "
                    "unless told otherwise.",
                    fill=t["muted"], size=11.5))
    out.append("</g></svg>")
    return "".join(out)


# -- footer -------------------------------------------------------------------

def footer(t: dict) -> str:
    width, height = 1000, 96
    out = [open_svg(width, height, ""), frame(width, height, t, radius=14),
           '<g clip-path="url(#clip)">']
    out.append(f'<defs><linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">'
               f'<stop offset="0%" stop-color="{t["accent"]}" stop-opacity="0"/>'
               f'<stop offset="35%" stop-color="{t["accent"]}" stop-opacity="0.9"/>'
               f'<stop offset="100%" stop-color="{t["accent"]}" stop-opacity="0"/>'
               f'</linearGradient></defs>')
    out.append(f'<line x1="0" y1="48" x2="1000" y2="48" stroke="url(#fade)" '
               f'stroke-width="1.4"/>')
    out.append(f'<circle cy="48" r="3" fill="{t["accent"]}" filter="url(#glow)">'
               f'<animate attributeName="cx" values="80;920;80" dur="9s" '
               f'repeatCount="indefinite"/>'
               f'<animate attributeName="opacity" values="0;1;1;0" dur="9s" '
               f'repeatCount="indefinite"/></circle>')
    out.append(text(500, 76, "github.com/RootX22", fill=t["faint"], size=11,
                    family=MONO, anchor="middle", spacing="2"))
    out.append("</g></svg>")
    return "".join(out)


def main() -> None:
    here = pathlib.Path(__file__).parent
    builders = {"header": header, "capabilities": capabilities,
                "pipeline": pipeline, "footer": footer}
    for name, build in builders.items():
        for theme, palette in THEMES.items():
            path = here / f"{name}-{theme}.svg"
            path.write_text(build(palette) + "\n", encoding="utf-8")
            print(f"wrote {path.name}  ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
