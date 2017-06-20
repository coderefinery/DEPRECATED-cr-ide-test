from swissutil.math import factorial
from pytest import raises

def test_factorial():
    # there is a significant bug in the factorial function
    # try calling factorial(-1)
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    with raises(ValueError):
        factorial(-1)
