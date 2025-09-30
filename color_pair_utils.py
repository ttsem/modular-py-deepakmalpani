def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'


def get_color_from_pair_number(pair_number, major_colors_list, minor_colors_list):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(minor_colors_list)
  if major_index >= len(major_colors_list):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(minor_colors_list)
  if minor_index >= len(minor_colors_list):
    raise Exception('Minor index out of range')
  return major_colors_list[major_index], minor_colors_list[minor_index]


def get_pair_number_from_color(major_colors_list, minor_colors_list,major_color, minor_color):
  try:
    major_index = major_colors_list.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = minor_colors_list.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(minor_colors_list) + minor_index + 1
