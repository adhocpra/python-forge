import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np

# ── Colour palette ──────────────────────────────────────────────────────────
BRAZIL  = "#009C3B"   # green
BRAZIL2 = "#FFDF00"   # yellow accent
MOROCCO = "#C1272D"   # red
MOROCCO2= "#006233"   # dark-green accent
BG      = "#0D1117"
PANEL   = "#161B22"
TEXT    = "#E6EDF3"
SUBTEXT = "#8B949E"
GRID    = "#21262D"

plt.rcParams.update({
    "figure.facecolor": BG,
    "axes.facecolor":   PANEL,
    "axes.edgecolor":   GRID,
    "axes.labelcolor":  TEXT,
    "xtick.color":      SUBTEXT,
    "ytick.color":      SUBTEXT,
    "text.color":       TEXT,
    "grid.color":       GRID,
    "grid.linestyle":   "--",
    "grid.alpha":       0.5,
    "font.family":      "DejaVu Sans",
})

# ── Raw data ────────────────────────────────────────────────────────────────
stats_labels = ["Total Shots", "Shots on Target", "Corners", "Fouls", "Saves", "Duels Won"]
brazil_vals  = [12, 5, 6, 16, 2, 53]
morocco_vals = [14, 3, 2, 14, 4, 62]

poss_brazil  = 51.3
poss_morocco = 48.7

pass_brazil_acc  = 87
pass_morocco_acc = 86
pass_brazil_tot  = 524
pass_morocco_tot = 493

xg_brazil  = 1.26
xg_morocco = 1.37

goal_times   = [21, 32]
goal_teams   = ["Morocco\nSaibari", "Brazil\nVinícius Jr."]
goal_colors  = [MOROCCO, BRAZIL]

viewership_labels = [
    "Mexico v\nS.Africa\n(FOX)",
    "Mexico v\nS.Africa\n(Telemundo)",
    "USA v\nParaguay\n(FOX)",
    "USA v\nParaguay\n(Telemundo)",
]
viewership_vals   = [6.31, 12.1, 15.99, 8.9]
view_colors       = ["#1F6FEB", "#A371F7", "#1F6FEB", "#A371F7"]

ranking_labels = ["FIFA Ranking", "Goals/Match", "xG/Game", "Avg Shots", "Goals Conceded", "Poss Avg (%)"]
brazil_profile  = [5,  1.8, 1.51, 13.4, 0.8, 58]
morocco_profile = [8,  1.5, 1.66, 14.5, 0.6, 57]

# ── Figure layout ────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(20, 24), facecolor=BG)
gs  = gridspec.GridSpec(4, 3, figure=fig, hspace=0.55, wspace=0.38)

# ── Helper: horizontal bar pair ──────────────────────────────────────────────
def hbar_pair(ax, labels, b_vals, m_vals, title):
    y    = np.arange(len(labels))
    h    = 0.35
    b1   = ax.barh(y + h/2, b_vals,  h, color=BRAZIL,  label="Brazil",  zorder=3)
    b2   = ax.barh(y - h/2, m_vals,  h, color=MOROCCO, label="Morocco", zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_title(title, fontsize=12, fontweight="bold", pad=8)
    ax.grid(axis="x", zorder=0)
    ax.legend(fontsize=9, loc="lower right")
    for bar, val in zip(b1, b_vals):
        ax.text(bar.get_width() + max(b_vals + m_vals)*0.02, bar.get_y() + bar.get_height()/2,
                str(val), va="center", fontsize=9, color=TEXT)
    for bar, val in zip(b2, m_vals):
        ax.text(bar.get_width() + max(b_vals + m_vals)*0.02, bar.get_y() + bar.get_height()/2,
                str(val), va="center", fontsize=9, color=TEXT)

# ── 1. Header banner ─────────────────────────────────────────────────────────
ax_hdr = fig.add_subplot(gs[0, :])
ax_hdr.set_facecolor(PANEL)
ax_hdr.set_xlim(0, 1)
ax_hdr.set_ylim(0, 1)
ax_hdr.axis("off")

ax_hdr.text(0.5, 0.82, "FIFA World Cup 2026™  ·  Group C  ·  Match 7",
            ha="center", va="center", fontsize=13, color=SUBTEXT)
ax_hdr.text(0.5, 0.50, "BRAZIL  1 – 1  MOROCCO",
            ha="center", va="center", fontsize=30, fontweight="bold", color=TEXT)
ax_hdr.text(0.5, 0.18,
            "MetLife Stadium, East Rutherford, NJ  ·  June 13, 2026  ·  Att: 80,663 / 82,500 (97.8%)",
            ha="center", va="center", fontsize=11, color=SUBTEXT)

goal_text = "* 21'  Ismael Saibari  (Morocco)   |   32'  Vinicius Junior  (Brazil)  *"
ax_hdr.text(0.5, -0.04, goal_text, ha="center", va="center", fontsize=11, color=TEXT,
            bbox=dict(boxstyle="round,pad=0.4", facecolor=GRID, edgecolor=GRID))

# ── 2. Match stats horizontal bars ──────────────────────────────────────────
ax1 = fig.add_subplot(gs[1, :2])
hbar_pair(ax1, stats_labels, brazil_vals, morocco_vals, "Match Statistics Comparison")

# ── 3. Possession donut ──────────────────────────────────────────────────────
ax2 = fig.add_subplot(gs[1, 2])
ax2.set_facecolor(PANEL)
sizes  = [poss_brazil, poss_morocco]
colors = [BRAZIL, MOROCCO]
wedges, _ = ax2.pie(sizes, colors=colors, startangle=90,
                    wedgeprops=dict(width=0.5, edgecolor=BG, linewidth=2))
ax2.text(0, 0.12, f"{poss_brazil}%",  ha="center", va="center", fontsize=16,
         fontweight="bold", color=BRAZIL)
ax2.text(0, -0.18, f"{poss_morocco}%", ha="center", va="center", fontsize=16,
         fontweight="bold", color=MOROCCO)
ax2.set_title("Ball Possession", fontsize=12, fontweight="bold", pad=10)
ax2.legend(["Brazil", "Morocco"], loc="lower center", fontsize=9,
           bbox_to_anchor=(0.5, -0.06))

# ── 4. xG comparison ─────────────────────────────────────────────────────────
ax3 = fig.add_subplot(gs[2, 0])
teams  = ["Brazil", "Morocco"]
xg_v   = [xg_brazil, xg_morocco]
xg_clr = [BRAZIL, MOROCCO]
bars   = ax3.bar(teams, xg_v, color=xg_clr, width=0.45, zorder=3,
                 edgecolor=BG, linewidth=1.5)
for bar, val in zip(bars, xg_v):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
             f"{val:.2f}", ha="center", fontsize=13, fontweight="bold", color=TEXT)
ax3.set_ylim(0, max(xg_v) * 1.35)
ax3.set_title("Expected Goals (xG)", fontsize=12, fontweight="bold")
ax3.set_ylabel("xG", fontsize=10)
ax3.grid(axis="y", zorder=0)

# ── 5. Pass accuracy grouped bars ────────────────────────────────────────────
ax4 = fig.add_subplot(gs[2, 1])
x      = np.arange(2)
w      = 0.35
b_tot  = ax4.bar(x - w/2, [pass_brazil_tot, pass_morocco_tot], w,
                 color=[BRAZIL, MOROCCO], zorder=3, label=["Brazil", "Morocco"],
                 edgecolor=BG, linewidth=1.2)
ax4_r  = ax4.twinx()
b_acc  = ax4_r.bar(x + w/2, [pass_brazil_acc, pass_morocco_acc], w,
                   color=[BRAZIL2, MOROCCO2], zorder=3, edgecolor=BG, linewidth=1.2)
ax4.set_xticks(x)
ax4.set_xticklabels(["Brazil", "Morocco"])
ax4.set_ylabel("Total Passes", color=SUBTEXT, fontsize=9)
ax4_r.set_ylabel("Accuracy %", color=SUBTEXT, fontsize=9)
ax4.set_title("Passes — Volume & Accuracy", fontsize=12, fontweight="bold")
ax4.grid(axis="y", zorder=0)
for bar, val in zip(b_tot, [pass_brazil_tot, pass_morocco_tot]):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
             str(val), ha="center", fontsize=10, fontweight="bold", color=TEXT)
for bar, val in zip(b_acc, [pass_brazil_acc, pass_morocco_acc]):
    ax4_r.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
               f"{val}%", ha="center", fontsize=10, fontweight="bold", color=TEXT)
p1 = mpatches.Patch(color=BRAZIL,  label="Brazil passes")
p2 = mpatches.Patch(color=MOROCCO, label="Morocco passes")
p3 = mpatches.Patch(color=BRAZIL2, label="Brazil acc%")
p4 = mpatches.Patch(color=MOROCCO2,label="Morocco acc%")
ax4.legend(handles=[p1, p2, p3, p4], fontsize=8, loc="lower right")

# ── 6. Goal timeline ─────────────────────────────────────────────────────────
ax5 = fig.add_subplot(gs[2, 2])
ax5.set_xlim(0, 95)
ax5.set_ylim(0, 1)
ax5.axhline(0.5, color=SUBTEXT, linewidth=2, zorder=1)
ax5.fill_between([0, 45], 0, 1, color=GRID, alpha=0.3, label="1st Half")
ax5.fill_between([45, 90], 0, 1, color=GRID, alpha=0.15, label="2nd Half")
for t, label, color in zip(goal_times, goal_teams, goal_colors):
    ax5.scatter(t, 0.5, s=280, color=color, zorder=5, edgecolors=BG, linewidths=1.5)
    ax5.text(t, 0.72 if color == MOROCCO else 0.22,
             f"{t}'", ha="center", fontsize=11, fontweight="bold", color=color)
    ax5.text(t, 0.84 if color == MOROCCO else 0.10,
             label, ha="center", fontsize=8, color=color)
ax5.axvline(45, color=SUBTEXT, linewidth=1, linestyle="--", alpha=0.6)
ax5.set_xticks([0, 15, 30, 45, 60, 75, 90])
ax5.set_xticklabels(["0'", "15'", "30'", "HT", "60'", "75'", "FT"])
ax5.set_yticks([])
ax5.set_title("Goal Timeline", fontsize=12, fontweight="bold")
bpatch = mpatches.Patch(color=BRAZIL,  label="Brazil")
mpatch = mpatches.Patch(color=MOROCCO, label="Morocco")
ax5.legend(handles=[bpatch, mpatch], fontsize=9, loc="upper right")

# ── 7. US Viewership bar chart ───────────────────────────────────────────────
ax6 = fig.add_subplot(gs[3, :2])
x_v  = np.arange(len(viewership_labels))
bars = ax6.bar(x_v, viewership_vals, color=view_colors, width=0.5,
               zorder=3, edgecolor=BG, linewidth=1.5)
for bar, val in zip(bars, viewership_vals):
    ax6.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
             f"{val}M", ha="center", fontsize=11, fontweight="bold", color=TEXT)
ax6.set_xticks(x_v)
ax6.set_xticklabels(viewership_labels, fontsize=10)
ax6.set_ylabel("US Viewers (millions)", fontsize=10)
ax6.set_title("2026 FIFA World Cup — US Viewership by Match & Network", fontsize=12, fontweight="bold")
ax6.grid(axis="y", zorder=0)
ax6.set_ylim(0, 20)
fox_p  = mpatches.Patch(color="#1F6FEB", label="FOX (English)")
tel_p  = mpatches.Patch(color="#A371F7", label="Telemundo (Spanish)")
ax6.legend(handles=[fox_p, tel_p], fontsize=10)
ax6.text(0.98, 0.95,
         "Brazil vs Morocco specific ratings\nnot yet published (match Jun 13)",
         transform=ax6.transAxes, ha="right", va="top", fontsize=8.5,
         color=SUBTEXT, style="italic",
         bbox=dict(boxstyle="round,pad=0.3", facecolor=GRID, edgecolor=GRID, alpha=0.7))

# ── 8. Attendance gauge ──────────────────────────────────────────────────────
ax7 = fig.add_subplot(gs[3, 2])
ax7.set_facecolor(PANEL)
ax7.set_xlim(0, 1)
ax7.set_ylim(0, 1)
ax7.axis("off")

attended = 80663
capacity = 82500
pct      = attended / capacity

# Background arc
theta_bg = np.linspace(np.pi, 0, 200)
ax7.plot(0.5 + 0.38 * np.cos(theta_bg), 0.35 + 0.38 * np.sin(theta_bg),
         color=GRID, linewidth=18, solid_capstyle="round")
# Fill arc proportional to attendance
theta_fill = np.linspace(np.pi, np.pi - pct * np.pi, 200)
ax7.plot(0.5 + 0.38 * np.cos(theta_fill), 0.35 + 0.38 * np.sin(theta_fill),
         color=BRAZIL, linewidth=18, solid_capstyle="round")

ax7.text(0.5, 0.35, f"{attended:,}", ha="center", va="center",
         fontsize=20, fontweight="bold", color=TEXT)
ax7.text(0.5, 0.16, f"of {capacity:,} capacity", ha="center", va="center",
         fontsize=10, color=SUBTEXT)
ax7.text(0.5, 0.04, f"{pct*100:.1f}% full", ha="center", va="center",
         fontsize=13, fontweight="bold", color=BRAZIL2)
ax7.set_title("Stadium Attendance\nMetLife Stadium, NJ", fontsize=12, fontweight="bold")

# ── Footer ───────────────────────────────────────────────────────────────────
fig.text(0.5, 0.01,
         "Sources: ESPN · FIFA.com · Opta Analyst · FWC Times · NBC Sports · Sports Media Watch · Morocco World News",
         ha="center", fontsize=8.5, color=SUBTEXT, style="italic")

plt.savefig("/home/pravat/brazil_morocco_wc2026.png",
            dpi=150, bbox_inches="tight", facecolor=BG)
print("Saved: /home/pravat/brazil_morocco_wc2026.png")
plt.show()
