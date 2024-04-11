# test_swap.py
from swap import swap_values
def test_swap_values():
    assert swap_values(3, 4) == (4, 3), "Values should be swapped"