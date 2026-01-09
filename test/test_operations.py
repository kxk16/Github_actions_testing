from src.math_operations import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(4,11) == 15
    assert add(1,6) == 7

def test_sub():
    assert sub(4,2) == 2
    assert sub(12,7) == 5
    assert sub(6,2) == 4
