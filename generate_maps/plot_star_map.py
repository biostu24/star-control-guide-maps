import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from plot_aspects import add_spheres_of_influence, add_grid_and_ticks

# Load data
data = pd.read_csv('data/star_data.csv')
n = len(data)

# Transform data
data['x'] = data['x'] / 10
data['y'] = data['y'] / 10

# Star colours
star_colour = pd.Series(['?'] * n)
star_colour[data['star_colour'] == 'RED'] = 'r'
star_colour[data['star_colour'] == 'ORANGE'] = '#c97302'
star_colour[data['star_colour'] == 'YELLOW'] = 'y'
star_colour[data['star_colour'] == 'GREEN'] = '#007500'
star_colour[data['star_colour'] == 'BLUE'] = '#2121c4'
star_colour[data['star_colour'] == 'WHITE'] = 'w'

# Star sizes
star_size = pd.Series([1.0] * n)
star_size[data['star_type'] == 'DWARF'] = 0.5
star_size[data['star_type'] == 'GIANT'] = 3
star_size[data['star_type'] == 'SUPER_GIANT'] = 8
star_glow = pd.Series([1.0] * n)
star_glow[data['star_type'] == 'DWARF'] = 3
star_glow[data['star_type'] == 'GIANT'] = 12
star_glow[data['star_type'] == 'SUPER_GIANT'] = 25

#### Plotting
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10,10))

# Data
ax.scatter(data['x'], data['y'], c=star_colour, s=star_glow, alpha=0.5, zorder=2)
ax.scatter(data['x'], data['y'], c=star_colour, s=star_size, alpha=1, zorder=2)

# Plot aspects
add_grid_and_ticks(ax)
add_spheres_of_influence(ax)

#plt.show()
fig.savefig('maps/star_map.png', dpi=100)
