import pytest

from common.solutions import Solution

@pytest.mark.parametrize("input,expected", 
    [[1, 1],
    [2, 6],
    [3, 90],
    [7, 681080400]],
    ids=["case 1", "case 2", "case 3", "case 4"])
def test_solutions(input: int, expected: int):
    actual = Solution.countOrders(input)
    assert actual == expected