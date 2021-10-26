# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
colors = {'red', 'green', 'blue'}
adj_matrix = {'WA': ['SA', 'NT'],
              'SA': ['WA', 'NT'],
              'NT': ['WA', 'SA']}
country_colors = {'WA': {'red', 'green', 'blue'},
                  'SA': {'red', 'green'},
                  'NT': {'green'}}
# adj_matrix = {'T': ['V'],
#               'WA': ['NT', 'SA'],
#               'NT': ['WA', 'Q', 'SA'],
#               'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
#               'Q': ['NT', 'SA', 'NSW'],
#               'NSW': ['Q', 'SA', 'V'],
#               'V': ['SA', 'NSW', 'T']}
# country_colors = {'WA': {'red'},
#                   'NT': {'red', 'blue', 'green'},
#                   'SA': {'red', 'blue', 'green'},
#                   'Q': {'green'},
#                   'NSW': {'red', 'blue', 'green'},
#                   'V': {'red', 'blue', 'green'},
#                   'T': {'red', 'blue', 'green'}}


def forward_check(country, color):
    for neighbour in adj_matrix[country]:
        if color in country_colors[neighbour] and len(country_colors[neighbour]) == 1:
            return False
    return True


def set_country_color(country, color):
    country_colors[country] = color
    for neighbour in adj_matrix[country]:
        if type(country_colors[neighbour]) == set:
            country_colors[neighbour].discard(color)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while sum(1 for x in country_colors.values() if type(x) == set):
        print(country_colors)
        # get the MRV:
        country = sorted([x for x in country_colors.keys() if type(country_colors[x]) == set], key=lambda x: len(country_colors[x]))[0]
        for color in country_colors[country]:
            if forward_check(country, color):
                set_country_color(country, color)
                break

        if type(country_colors[country]) == set:
            print('Cannot solve problem')
            raise SystemExit
    print(country_colors)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
