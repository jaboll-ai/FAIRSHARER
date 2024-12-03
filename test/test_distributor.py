import sys
import os
sys.path.append(os.getcwd())

from distributor import fair_sharer
import pytest

@pytest.mark.parametrize("values, num_iterations, result", [
    ([0, 1000, 800, 0], 1, [100, 800, 900, 0]), 
    ([0, 1000, 800, 0], 2, [100, 890, 720, 90]),])
def test_fairsharer(values, num_iterations, result):
    assert fair_sharer(values, num_iterations) == result
