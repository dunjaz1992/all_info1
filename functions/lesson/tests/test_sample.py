from lesson import add_one, division
import pytest 


# def test_answer():
#     assert add_one(3) == 4
#     # assert add_one(8) == 8

# def test_division():
#     assert division(8, 4) == 1
# def test_division2():
#     with pytest.raises(ZeroDivisionError):
#         division(3, 0)

def add(x: int, y: int) -> int:
    return x + y 
def test_add():
    test_case = [[1, 2, 3], [1, 2, 5], [3, 4, 7]]
    for i in test_case: 
        assert add(i[0], i[1]) == i[2]