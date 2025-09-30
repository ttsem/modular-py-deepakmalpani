
from helpers.reference_manual import return_colors_reference_manual


def test_colors_reference_manual():
    actual = return_colors_reference_manual()
    
    assert actual['White Blue'] == 1