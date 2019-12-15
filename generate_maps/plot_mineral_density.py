import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
from plot_aspects import add_spheres_of_influence, add_grid_and_ticks
import matplotlib.patches as mpatches
from CurvedText import CurvedText


def plot_fun(dat, title, outfile, bio=False, partial_map=False):
    # Colour map
    if bio:
        colours = ['#1f1f1f', (0.2,1,0)]
        data = dat['bio']['sum']
    else:
        colours = ['#1f1f1f', '#2c268a', '#802f95', '#ea3d38', '#e77d02', '#e6c72f', '#ffffff']
        data = dat['filt_mineral']['sum']
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list('test', colours, N=250)

    # Star size modifier
    if partial_map:
        size_mod = 5.0
    else:
        size_mod = 1.0

    # Plot
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 10))

    fig.subplots_adjust(left=0.03, right=1.08, top=0.978, bottom=0.03)
    pos = ax.scatter(dat['x']['min'], dat['y']['min'], c=data,
                     cmap=cmap, s=star_size*size_mod, alpha=1, zorder=2)
    fig.colorbar(pos, ax=ax, aspect=50)
    ax.set_title(title)

    # Plot aspects
    add_grid_and_ticks(ax, partial_map)
    add_spheres_of_influence(ax, grey_theme=True, partial_map=partial_map)

    if partial_map:
        # Add 200 hyperspace sphere
        circle = mpatches.Circle((175.2, 145.0), 200, fill=False, color='#c2c2c2', zorder=1, ls=(0, (10,15)))
        ax.add_patch(circle)
        N = 100
        curve = [
            -np.cos(np.linspace(0,2*np.pi,N))*201+175.2,
            np.sin(np.linspace(0,2*np.pi,N))*201+145.0,
        ]

        text = CurvedText(
            x=curve[0],
            y=curve[1],
            text= (' '*40) + 'Within 200 hyperspace units of Sol',
            va='bottom',
            axes=ax,
            fontsize=12
        )

    fig.savefig(outfile, dpi=100)


# Load data
data = pd.read_csv('data/planet_data.csv')

# Distance to sol
sol = (175.2, 145.0)
data['dist_to_sol'] = ((data['x'] - sol[0])**2 +  (data['y'] - sol[1])**2) ** 0.5

# Mineral calc
data['filt_mineral'] = data['total_ru']

# Star aggregate
agg = data.groupby('star_name').agg(['min', 'sum'])
n_stars = len(agg)

# Star sizes
star_size = pd.Series([2] * n_stars, index = agg.index)
star_size[agg['star_type']['min'] == 'dwarf'] = 4  # 0.5
star_size[agg['star_type']['min'] == 'giant'] = 14  # 3
star_size[agg['star_type']['min'] == 'super giant'] = 25  # 8

# Plot total RU
plot_fun(agg, 'Star total RU', 'maps/star_map_total_RU.png')

# Filter
data['filt_mineral'] = data['total_ru']#data['rare_earth'] + data['precious'] + data['radioactive'] + data['exotic']

data.loc[data['tectonics'].gt(4), 'filt_mineral'] = 0
data.loc[data['weather'].gt(3), 'filt_mineral'] = 0
data.loc[data['temp'].gt(200), 'filt_mineral'] = 0
data.loc[data['dist_to_sol'].gt(200), 'filt_mineral'] = 0

agg = data.groupby('star_name').agg(['min', 'sum'])

# Plot safe stars
plot_fun(agg, 'Top early stars - RU', 'maps/star_map_top_early_RU.png', partial_map=True)

# Plot bio
plot_fun(agg, 'Biological units', 'maps/star_map_bio_units.png', bio=True)

# Plot bio from safe stars
data.loc[data['tectonics'].gt(4), 'bio'] = 0
data.loc[data['weather'].gt(3), 'bio'] = 0
data.loc[data['temp'].gt(200), 'bio'] = 0
data.loc[data['dist_to_sol'].gt(200), 'bio'] = 0

agg = data.groupby('star_name').agg(['min', 'sum'])

plot_fun(agg, 'Top early stars - biological units', 'maps/star_map_top_early_bio.png', bio=True, partial_map=True)
