from helpers.reference_manual import return_colors_reference_manual
from tests.converters.test_color_to_pair_number import test_pair_to_number
from tests.converters.test_pair_number_to_color import test_number_to_pair
from tests.helpers.test_reference_manual import test_colors_reference_manual

if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  test_colors_reference_manual()
  print(return_colors_reference_manual())
  print('Done :)')
