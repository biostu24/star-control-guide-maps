# These helper function add various features used all the maps

import matplotlib.patches as mpatches
import numpy as np

def add_spheres_of_influence(ax, grey_theme=False, partial_map=False):
    cyan='#034f6b'
    blue='#000266'
    purple='#5e0053'
    green='#005e00'
    grey='#4a4a4a'
    orange='#733b00'
    red='#630202'
    sphere_data = [
        # 0             1     2     3     4    5      6    7
        ["Arilou",      438,  6372, 250,  0,   0,     90,  blue],
        ["Druuge",      9500, 2792, 1400, -50, 20,    120, red],
        ["Ilwrath",     48,   1700, 1410, 450, 0,     60,  purple],
        ["Kohr-Ah",     6000, 6250, 2666, 110, 220,   80,  grey],
        ["Mycon",       6392, 2200, 1070, -50, 0,     80,  purple],
        ["Orz",         3608, 2637, 333,  -40, -20,   45,  purple],
        ["Pkunk",       502,  401,  666,  0,   -35,   20,  cyan],
        ["Spathi",      2549, 3600, 1000, 0,   -8,    120, orange],
        ["Supox",       7468, 9246, 333,  10,  15,    120, orange],
        ["Thraddash",   2535, 8358, 833,  -40, -25,   120, cyan],
        ["Umgah",       1798, 6000, 833,  0,    50,   90,  purple],
        ["Ur-Quan",     5750, 6000, 2666, -150, -200, 80,  green],
        ["Utwig",       8534, 8797, 666,  25,   20,   45,  cyan],
        ["VUX",         4412, 1558, 900,  20,   0,    90,  blue],
        ["Yehat",       4970, 40,   750,  -25,  50,   80,  purple],
        ["ZoqFot", 3761, 5333, 320,  0,   -40,   0,   red],
    ]

    if partial_map:
        sphere_data[13][0] = ''

    for sp in sphere_data:
        cx, cy = sp[1] * 0.1, sp[2] * 0.1
        size = sp[3] * 0.1
        tx, ty = (sp[1] + sp[4]) * 0.1, (sp[2] + sp[6]) * 0.1
        colour = sp[7]
        cname = sp[0]

        if grey_theme:
            colour = '#242424'
            name = ''

        circle = mpatches.Circle((cx, cy), size, fill=False, color=colour, zorder=1)
        ax.add_patch(circle)
        ax.text(tx, ty, cname, fontsize=15, color=colour,
                horizontalalignment='center',
                #verticalalignment='center',
                zorder=1)

def add_grid_and_ticks(ax, partial_map=False):
    major_ticks = np.arange(0, 1001, 50)
    minor_ticks = np.arange(0, 1001, 10)
    axis_lab = ['', '', '100', '', '200', '', '300', '', '400', '', '500', '',
                '600', '', '700', '', '800', '', '900', '', '']
    ax.set_xticks(major_ticks)
    ax.set_yticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(c='#0d0d0d')
    ax.set_axisbelow(True)
    ax.set_xticklabels(axis_lab)
    ax.set_yticklabels(axis_lab)

    if partial_map:
        ax.set_xlim([0, 400])
        ax.set_ylim([0, 400])
    else:
        ax.set_xlim([0, 1000])
        ax.set_ylim([0, 1000])
