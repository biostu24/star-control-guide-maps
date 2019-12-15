# generate_maps
This code-base takes world data extracted from Ur-Quan Masters (UQM) 
and generates star maps shown density of minerals and biological information
within Star Control 2 space. These maps are by within by an online UQM guide and 
can be found [here](https://wiki.uqm.stack.nl/Walkthrough#Other_Useful_Information)

## Prerequisites
 * Python 3.6 or greater
 * Python packages installed: `pip`, `virtualenv` 

This README is written for Linux but the codebase will run under other 
operating systems, some changes to the syntax may be required.

## Setup
A python virtual environment is highly recommended for this project.
This can be set up using the following:
```
python3.6 -m virtualenv venv &&
source venv/bin/activate
```

Next install required packages
```
python -m pip install -r requirements.txt
```

## Parse the debugging data from the UQM game
```
python parse_planets.py &&
python parse_stars.py
```

## Generate the maps

```
python plot_star_map.py &&
python plot_mineral_density.py
```
