"""Shared plotting helpers for the guide's diagrams.

Every figure in the notebook is built from the same few pieces: a canvas,
rounded boxes, larger frames, arrows, and small annotations. Each discipline
keeps one fixed, colorblind-safe color so the figures stay readable side by
side: prompt is blue, context orange, harness teal, loop amber, graph magenta.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

C = {
    "prompt":  "#2a78d6",   # blue
    "context": "#eb6834",   # orange
    "harness": "#1baf7a",   # teal
    "loop":    "#eda100",   # amber
    "graph":   "#e87ba4",   # magenta
}
INK, INK2, MUTED, SURFACE = "#0b0b0b", "#52514e", "#898781", "#fcfcfb"

plt.rcParams.update({
    "figure.facecolor": SURFACE,
    "axes.facecolor":   SURFACE,
    "figure.dpi":       100,
})


def tint(color, alpha=0.10):
    """A light wash of a discipline color, used as box fill."""
    r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
    return (r / 255, g / 255, b / 255, alpha)


def canvas(w, h, xlim, ylim):
    """A blank, axis-free figure to draw a diagram on."""
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    return ax


def box(ax, x, y, w, h, label, color=INK2, sub=None, fs=11, lw=1.6, ls="-"):
    """A rounded node with a bold label and an optional sub-caption."""
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.10",
        linewidth=lw, linestyle=ls, edgecolor=color, facecolor=tint(color)))
    if sub is None:
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=fs, fontweight="bold", color=INK)
    else:
        ax.text(x + w / 2, y + h * 0.66, label, ha="center", va="center",
                fontsize=fs, fontweight="bold", color=INK)
        ax.text(x + w / 2, y + h * 0.30, sub, ha="center", va="center",
                fontsize=fs - 2.5, color=INK2)


def frame(ax, x, y, w, h, label, color, sub="", ls="-"):
    """An unfilled boundary that groups other elements, labeled in its top corners."""
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.16",
        linewidth=2.0, linestyle=ls, edgecolor=color, facecolor="none"))
    ax.text(x + 0.30, y + h - 0.34, label, fontsize=11.5,
            fontweight="bold", color=INK, ha="left", va="center")
    if sub:
        ax.text(x + w - 0.30, y + h - 0.34, sub, fontsize=9.5,
                color=INK2, ha="right", va="center")


def arrow(ax, p1, p2, rad=0.0, color=MUTED, lw=1.5, style="->", shrink=5):
    """A straight or gently curved connector between two points."""
    ax.add_patch(FancyArrowPatch(
        p1, p2, arrowstyle=style, mutation_scale=13, linewidth=lw,
        color=color, shrinkA=shrink, shrinkB=shrink,
        connectionstyle="arc3,rad={}".format(rad)))


def note(ax, x, y, text, fs=9, ha="center", style="italic"):
    """A small secondary annotation, usually an edge label."""
    ax.text(x, y, text, ha=ha, va="center", fontsize=fs,
            color=INK2, fontstyle=style)


def title(ax, x, y, text, fs=16):
    """The figure heading."""
    ax.text(x, y, text, ha="center", va="center",
            fontsize=fs, fontweight="bold", color=INK)
