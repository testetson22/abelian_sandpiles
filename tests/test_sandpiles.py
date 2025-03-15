from sandpiles.sandpiles import *
import pytest
import numpy as np


@pytest.mark.parametrize("x,y,z,center_x,center_y", [
    (5, 5, 8, 2, 2),
    (10, 10, 64, 5, 5),
    (10, 5, 64, 5, 2),
    (40, 40, 128, 20, 20),
    (40, 40, 1028, 20, 20),
    (120, 120, 1028, 60, 60),
    (120, 100, 1028, 60, 50)
])
def test_sandpile_center_point(x, y, z, center_x, center_y):
    sandpile = SandPile(x, y, z)
    assert sandpile.get_sandpile_center_point() == (center_x, center_y)
    

# Formatting could be better, but clearly displaying the expected result is important
@pytest.mark.parametrize("x,y,z,expected_sandpile", [
    (5, 5, 0, [[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]),
    (5, 5, 8, [[0, 0, 0, 0, 0],
               [0, 0, 2, 0, 0],
               [0, 2, 0, 2, 0],
               [0, 0, 2, 0, 0],
               [0, 0, 0, 0, 0]]),
    (5, 5, 16, [[0, 0, 1, 0, 0],
                [0, 2, 1, 2, 0],
                [1, 1, 3, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]]),
    (10, 5, 16, [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 2, 1, 2, 0],
                 [1, 1, 3, 1, 1],
                 [0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]),
    (10, 10, 48, [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                  [0, 0, 0, 2, 1, 3, 1, 2, 0, 0],
                  [0, 0, 0, 3, 1, 2, 1, 3, 0, 0],
                  [0, 0, 1, 0, 3, 1, 3, 0, 1, 0],
                  [0, 0, 0, 2, 2, 1, 2, 2, 0, 0],
                  [0, 0, 0, 0, 1, 2, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
])
def test_abelian_sandpile(x, y, z, expected_sandpile):
    sandpile = SandPile(x, y, z)
    abelian_sandpile = sandpile.apply_gravity()
    np.testing.assert_array_equal(abelian_sandpile, expected_sandpile)
    
    
@pytest.mark.parametrize("x,y,z,exception_value", [
    (5, -1, 0, "Sandpile array dimensions must be greater than zero"),
    (5, 0, 0, "Sandpile array dimensions must be greater than zero"),
    (0, -1, 0, "Sandpile array dimensions must be greater than zero"),
    (-5, "5", 0, "Sandpile array dimensions and pile height must be int type")
])
def test_abelian_sandpile_exceptions(x, y, z, exception_value):
    with pytest.raises(Exception) as exp:
        SandPile(x, y, z)
    assert str(exp.value) == exception_value
