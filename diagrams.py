"""The notebook's seven figures, one function per diagram.

Layout only: the shared colors and drawing primitives are in utils.py.
"""

import matplotlib.pyplot as plt

from utils import C, INK, INK2, canvas, box, frame, arrow, note, title


def nesting():
    """How the five disciplines nest."""
    ax = canvas(12, 7.6, (0, 12), (0, 7.9))
    title(ax, 6, 7.55, "How the five disciplines nest")

    frame(ax, 0.35, 0.35, 11.30, 6.60, "Harness", C["harness"],
          "tools · permissions · validation · logging · recovery")
    frame(ax, 0.95, 0.95, 10.10, 5.00, "Graph", C["graph"],
          "routes work between specialized steps")
    frame(ax, 1.55, 1.55, 8.90, 3.55, "Loop", C["loop"],
          "observe → act → evaluate · repeat")

    box(ax, 2.20, 3.05, 2.60, 0.95, "Prompt", C["prompt"], sub="what to do")
    box(ax, 2.20, 1.90, 2.60, 0.95, "Context", C["context"], sub="what to know")
    box(ax, 6.70, 2.35, 2.90, 1.30, "Model", INK, sub="reasoning and generation", fs=12)

    arrow(ax, (4.80, 3.50), (6.70, 3.20), rad=-0.10)
    arrow(ax, (4.80, 2.40), (6.70, 2.80), rad=0.10)
    plt.show()


def prompt_anatomy():
    """The five parts of a strong prompt."""
    ax = canvas(13, 3.4, (0, 13), (0, 3.5))
    title(ax, 6.5, 3.15, "Anatomy of a strong prompt")

    parts = [
        ("Role",            '"a senior Python engineer"'),
        ("Objective",       '"find and fix the defect"'),
        ("Inputs",          '"code + failing test"'),
        ("Constraints",     '"keep the public API"'),
        ("Output contract", '"diagnosis, fix, tests"'),
    ]
    w, gap, y = 2.24, 0.32, 0.95
    for i, (name, example) in enumerate(parts):
        x = 0.35 + i * (w + gap)
        box(ax, x, y, w, 1.40, name, C["prompt"], sub=example, fs=11.5)
        if i:
            arrow(ax, (x - gap, y + 0.70), (x, y + 0.70), shrink=2)
    plt.show()


def context_pipeline():
    """Sources feeding the retrieve/filter/rank/compress/insert pipeline."""
    ax = canvas(13.4, 6.0, (0, 13.4), (0, 6.2))
    title(ax, 6.7, 5.85, "The context-engineering pipeline")

    sources = ["Conversation", "User profile", "Knowledge base", "Tool results"]
    for i, label in enumerate(sources):
        box(ax, 0.40, 4.35 - i * 1.10, 2.30, 0.85, label, INK2, fs=10.5)

    stages = ["Retrieve", "Filter", "Rank", "Compress", "Insert"]
    sw, sy = 1.62, 3.00
    xs = [3.50 + i * 1.92 for i in range(5)]
    for x, label in zip(xs, stages):
        box(ax, x, sy, sw, 0.90, label, C["context"], fs=10.5)
    for x1, x2 in zip(xs, xs[1:]):
        arrow(ax, (x1 + sw, sy + 0.45), (x2, sy + 0.45), shrink=2)

    for i in range(4):
        y = 4.35 - i * 1.10 + 0.42
        arrow(ax, (2.70, y), (3.50, sy + 0.45), rad=-0.12 if y > sy else 0.12)

    box(ax, 9.60, 0.80, 3.30, 1.20, "Model context window", INK, fs=11.5, lw=2.0)
    arrow(ax, (xs[4] + sw / 2, sy), (11.25, 2.00), rad=-0.15)
    note(ax, 6.55, 1.35, "only what survives the pipeline\nreaches the model", fs=9.5)
    plt.show()


def harness():
    """The components surrounding the model."""
    ax = canvas(12, 7.0, (0, 12), (0, 7.5))
    title(ax, 6, 7.15, "The agent harness")

    box(ax, 4.70, 2.95, 2.60, 1.25, "AI model", INK, fs=13, lw=2.0)

    components = [
        (0.70, 5.50, "Tools and APIs"),
        (4.65, 5.50, "Memory and state"),
        (8.60, 5.50, "Permissions"),
        (0.70, 0.85, "Validation"),
        (4.65, 0.85, "Logging"),
        (8.60, 0.85, "Retries and recovery"),
    ]
    for x, y, label in components:
        box(ax, x, y, 2.70, 0.95, label, C["harness"], fs=10.5)

    links = [
        ((2.05, 5.50), (4.90, 4.20)),
        ((6.00, 5.50), (6.00, 4.20)),
        ((9.95, 5.50), (7.10, 4.20)),
        ((2.05, 1.80), (4.90, 2.95)),
        ((6.00, 1.80), (6.00, 2.95)),
        ((9.95, 1.80), (7.10, 2.95)),
    ]
    for p1, p2 in links:
        arrow(ax, p1, p2, style="<->", shrink=3)
    plt.show()


def agent_loop():
    """Observe/decide/act/evaluate, with the stop exit."""
    ax = canvas(9, 8.2, (-4.5, 4.5), (-4.4, 4.0))
    title(ax, 0, 3.72, "The agent loop")

    nodes = {
        "Observe":  (0.00,  2.55),
        "Decide":   (2.75,  0.10),
        "Act":      (0.00, -2.35),
        "Evaluate": (-2.75, 0.10),
    }
    for label, (cx, cy) in nodes.items():
        box(ax, cx - 0.95, cy - 0.43, 1.90, 0.86, label, C["loop"], fs=11.5)

    hops = [
        ((0.85,  2.15), (2.60,  0.75)),    # Observe -> Decide
        ((2.60, -0.55), (0.85, -1.95)),    # Decide  -> Act
        ((-0.85, -1.95), (-2.60, -0.55)),  # Act     -> Evaluate
        ((-2.60,  0.75), (-0.85,  2.15)),  # Evaluate -> Observe
    ]
    for p1, p2 in hops:
        arrow(ax, p1, p2, rad=-0.22, lw=1.8)

    ax.text(0, 0.42, "Goal", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)
    note(ax, 0, -0.18, "go around again until\na stop condition is met", fs=9.5)

    box(ax, -4.35, -3.85, 1.90, 0.86, "Stop", INK2, fs=11.5)
    arrow(ax, (-3.05, -0.35), (-3.40, -2.95), rad=0.18)
    note(ax, -3.90, -1.60, "stop condition\nmet", fs=8.5, ha="center")
    plt.show()


def email_graph():
    """The inbound-email workflow graph."""
    ax = canvas(13, 9.2, (0, 13), (0, 9.6))
    title(ax, 6.5, 9.25, "Example workflow graph: inbound email")

    G = C["graph"]
    box(ax, 5.20, 8.00, 2.60, 0.80, "Receive email", G)
    box(ax, 5.40, 6.60, 2.20, 0.80, "Classify", G)
    box(ax, 1.30, 5.20, 2.00, 0.80, "Sales", G)
    box(ax, 5.50, 5.20, 2.00, 0.80, "Support", G)
    box(ax, 9.70, 5.20, 2.00, 0.80, "Spam", G)
    box(ax, 5.30, 3.80, 2.40, 0.80, "Retrieve account", G)
    box(ax, 9.70, 3.80, 2.00, 0.80, "Archive", INK2)
    box(ax, 3.40, 2.40, 2.20, 0.80, "Draft reply", G)
    box(ax, 3.30, 1.00, 2.40, 0.80, "Human approval", INK2, ls="--")
    box(ax, 7.20, 1.00, 2.00, 0.80, "Send", G)

    arrow(ax, (6.50, 8.00), (6.50, 7.40), shrink=3)
    arrow(ax, (5.75, 6.60), (2.60, 6.00), rad=0.12, shrink=3)
    arrow(ax, (6.50, 6.60), (6.50, 6.00), shrink=3)
    arrow(ax, (7.25, 6.60), (10.40, 6.00), rad=-0.12, shrink=3)
    note(ax, 3.30, 6.62, "sales inquiry", fs=9)
    note(ax, 7.30, 6.30, "support request", fs=9)
    note(ax, 9.75, 6.62, "junk", fs=9)

    arrow(ax, (2.30, 5.20), (4.05, 3.20), rad=0.15, shrink=3)
    arrow(ax, (6.50, 5.20), (6.50, 4.60), shrink=3)
    arrow(ax, (10.70, 5.20), (10.70, 4.60), shrink=3)
    arrow(ax, (6.20, 3.80), (4.95, 3.20), rad=0.10, shrink=3)
    arrow(ax, (4.50, 2.40), (4.50, 1.80), shrink=3)
    arrow(ax, (5.70, 1.40), (7.20, 1.40), shrink=3)
    note(ax, 6.45, 1.62, "approved", fs=9)
    note(ax, 10.70, 3.32, "terminal node", fs=8.5)
    plt.show()


def coding_agent():
    """The full coding-agent architecture, all five layers at once."""
    ax = canvas(14, 8.4, (0, 14), (0, 8.7))
    title(ax, 7, 8.35, "A complete coding agent, seen through all five disciplines")

    frame(ax, 0.30, 0.30, 13.40, 7.55, "Harness", C["harness"],
          "file tools · terminal · git · test runner · sandbox · logging")

    G = C["graph"]
    box(ax, 0.90, 4.60, 1.90, 0.90, "Triage", G)
    box(ax, 3.35, 5.75, 2.20, 0.90, "Frontend fix", G)
    box(ax, 3.35, 3.45, 2.20, 0.90, "Backend fix", G)

    frame(ax, 6.10, 3.30, 7.20, 3.70, "Loop", C["loop"],
          "repeat until tests pass", ls="--")
    box(ax, 6.65, 4.55, 2.20, 0.90, "Implement", G)
    box(ax, 9.85, 4.55, 2.20, 0.90, "Run tests", G)
    arrow(ax, (8.85, 5.15), (9.85, 5.15), shrink=3)
    arrow(ax, (10.95, 4.55), (7.75, 4.55), rad=-0.30, shrink=6)
    note(ax, 9.35, 3.78, "failures", fs=8.5)

    arrow(ax, (1.85, 5.50), (3.35, 6.20), rad=-0.10, shrink=4)
    arrow(ax, (1.85, 4.60), (3.35, 3.90), rad=0.10, shrink=4)
    note(ax, 2.35, 6.12, "UI bug", fs=8.5)
    note(ax, 2.30, 3.90, "server bug", fs=8.5)
    arrow(ax, (5.55, 6.20), (6.65, 5.30), rad=-0.10, shrink=4)
    arrow(ax, (5.55, 3.90), (6.65, 4.80), rad=0.10, shrink=4)

    box(ax, 10.30, 1.55, 2.60, 0.90, "Review and verify", G, fs=10.5)
    arrow(ax, (11.60, 4.55), (11.60, 2.45), shrink=6)
    note(ax, 12.30, 3.40, "tests pass", fs=8.5)

    box(ax, 6.60, 1.55, 2.40, 0.90, "Human approval", INK2, ls="--", fs=10.5)
    arrow(ax, (10.30, 2.00), (9.00, 2.00), shrink=3)
    box(ax, 2.70, 1.55, 2.60, 0.90, "Create pull request", G, fs=10.5)
    arrow(ax, (6.60, 2.00), (5.30, 2.00), shrink=3)
    note(ax, 5.95, 2.22, "approved", fs=8.5)

    box(ax, 0.75, 2.85, 1.55, 0.62, "Prompt", C["prompt"], fs=9.5)
    box(ax, 0.75, 2.05, 1.55, 0.62, "Context", C["context"], fs=9.5)
    note(ax, 0.78, 1.45, "together they shape every", fs=8, ha="left")
    note(ax, 0.78, 1.15, "model call in the graph", fs=8, ha="left")
    plt.show()
