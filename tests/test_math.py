from swissutil.math import factorial

import pytest

def test_factorial():
    # There is a significant bug in the factorial function
    # Try calling factorial(-1)
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    with pytest.raises(ValueError):
        factorial(-1)
