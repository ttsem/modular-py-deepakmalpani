from constants import MAJOR_COLORS, MINOR_COLORS


def get_pair_number_from_color(major_color, minor_color, major_colors_list = MAJOR_COLORS, minor_colors_list = MINOR_COLORS):
  try:
    major_index = major_colors_list.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = minor_colors_list.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(minor_colors_list) + minor_index + 1