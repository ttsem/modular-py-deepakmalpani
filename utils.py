from constants import MAJOR_COLORS, MINOR_COLORS
from converters import get_pair_number_from_color


def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'


def print_colors_reference_manual(major_color_list = MAJOR_COLORS, minor_color_list = MINOR_COLORS):
    result = {}
    for major_color in major_color_list:
        for minor_color in minor_color_list:
            result[color_pair_to_string(major_color, minor_color)] = get_pair_number_from_color(major_color, minor_color)
    
    print(result)