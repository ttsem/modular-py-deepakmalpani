from converters.color_to_pair_number import get_pair_number_from_color

def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pair_number_from_color( major_color, minor_color)
  assert(pair_number == expected_pair_number)