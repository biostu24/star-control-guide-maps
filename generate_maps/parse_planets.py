# This function parses the debug output of UQM to csv format

def parse_planets(out_file_planets = 'data/planet_data.csv',
                  planet_file = 'data/PlanetInfo',
                  mineral_file = 'data/sub_minerals.txt'):

    # Parse sub minerals
    with open(mineral_file) as f:
        mineral_values = [1, 2, 3, 4, 5, 6, 8, 25]
        sub_minerals = []

        for line in f:
            mineral_line = []
            if 'minz_s|' in line:
                line = line.replace('minz_s|', '')
                mineral_amounts = line.split('|')

                for i in range(8):
                    mineral_value = int(mineral_amounts[i]) * mineral_values[i]
                    mineral_line.append(str(mineral_value))

                sub_minerals.append(mineral_line)

    # Parse planets
    planet_columns = []
    planets = []
    with open(planet_file) as f:
        # Variables to collect
        x = 0
        y = 0
        star_name = ''
        star_colour = ''
        star_type = ''
        parent_planet = ''
        object_name = ''
        world_type = ''
        tectonics = 0
        weather = 0
        temp = 0
        bio = 0
        total_RU = 0
        dist_to_sol = 0

        lines = f.read().split('\n')
        lines.reverse()

        line = lines.pop()
        while lines:
            #######################
            ### Parse star data ###
            #######################
            #print(line)

            # Star: Name
            star_name, line = line.split('(')
            star_name = star_name.strip()

            # Star: coords
            coords, line = line.split(')')
            x, y = coords.replace(' ', '').split(',')

            # Star: type
            if 'super giant' in line:
                star_type = 'super giant'
            elif 'giant' in line:
                star_type = 'giant'
            elif 'dwarf' in line:
                star_type = 'dwarf'

            # Star: colour
            star_colour = [i for i in line.split(' ') if len(i) > 0]
            star_colour = star_colour[0]

            ###############################
            ### Parse planets and moons ###
            ###############################
            line = lines.pop()
            objects_loop = True
            while objects_loop:
                # Determine type
                if 'Moon' in line:
                    is_moon = True
                else:
                    is_moon = False

                # Parse object header
                parts = [i for i in line.replace('- ', '').split(' ') if len(i) > 0]
                object_name = parts[1]
                del parts[0:2]
                if is_moon:
                    object_name = parent_planet + object_name
                else:
                    parent_planet = object_name
                world_type = ' '.join(parts)

                # Parse object
                sub_object_loop = True
                while sub_object_loop:
                    line = lines.pop()

                    if 'Tectonics:' in line:
                        tectonics = line.replace('Tectonics:', '').replace(' ', '')

                    if 'Weather:' in line:
                        weather = line.replace('Weather:', '').replace(' ', '')

                    if 'Temp:' in line:
                        temp = line.replace('Temp:', '').replace(' ', '')

                    if 'DistToSun:' in line:
                        dist_to_sol = line.replace('DistToSun:', '').replace(' ', '')

                    if 'Bio:' in line:
                        parts = [i for i in line.split(' ') if len(i) > 0]
                        bio = parts[1]
                        total_RU = parts[3]
                        sub_object_loop = False
                        line = lines.pop()

                if '- ' not in line:
                    objects_loop = False

                # Debug

                planets.append([star_name,
                                x,
                                y,
                                star_colour,
                                star_type,
                                object_name,
                                world_type,
                                tectonics,
                                weather,
                                temp,
                                bio,
                                total_RU,
                                dist_to_sol])


    print(len(sub_minerals))
    print(len(planets))

    header = ['star_name',
              'x',
              'y',
              'star_colour',
              'star_type',
              'object_name',
              'world_type',
              'tectonics',
              'weather',
              'temp',
              'bio',
              'total_ru',
              'dist_to_parent_star',
              'common',
              'corrosive',
              'base_metal',
              'noble',
              'rare_earth',
              'precious',
              'radioactive',
              'exotic']

    with open(out_file_planets, 'w') as f:
        # Header
        f.write(','.join(header) + '\n')

        # Data
        for a, b in zip(planets, sub_minerals):
            data = a + b
            f.write(','.join(data) + '\n')




if __name__ == '__main__':
    parse_planets()
