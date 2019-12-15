# This function parses the debug output of UQM to csv format

def parse_stars(out_file_stars = 'data/star_data.csv',
                star_file = 'data/stars'):
    # Parse stars
    star_columns = ['x', 'y', 'star_type', 'star_colour']
    stars = []
    with open(star_file) as f:
        for line in f:
            # Clean out spaces
            line = line.replace(' ','')

            # Skip to data
            if not line.startswith('\t{'):
                continue

            # Remove unwanted characters
            line = line.replace('{', '').replace('}', '').replace('\t', '').replace('(', ',').replace(')', '')

            # Get data values and drop unwanted items
            parts = line.split(',')
            del parts[2]
            parts = parts[0:4]

            # Clean values
            parts[2] = parts[2].replace('_STAR', '')
            parts[3] = parts[3].replace('_BODY', '')

            stars.append(parts)

        with open(out_file_stars, 'w') as f2:
            f2.write('x,y,star_type,star_colour\n')
            for line in stars:
                f2.write(','.join(line) + '\n')

if __name__ == '__main__':
    parse_stars()
