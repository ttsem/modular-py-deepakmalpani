from constants import MAJOR_COLORS, MINOR_COLORS

def get_color_from_pair_number(pair_number, major_colors_list = MAJOR_COLORS, minor_colors_list = MINOR_COLORS):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(minor_colors_list)
  if major_index >= len(major_colors_list):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(minor_colors_list)
  if minor_index >= len(minor_colors_list):
    raise Exception('Minor index out of range')
  return major_colors_list[major_index], minor_colors_list[minor_index]


