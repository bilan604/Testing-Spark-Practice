import pytest
from practice_code.house_robber import HouseRobber


@pytest.mark.parametrize("input,expected", 
    [[[1,2,3,1], 4],
    [[2,7,9,3,1], 12]],
    ids=["case 1", "case 2"])
def test_parse(input: str, expected: int):
    actual = HouseRobber.rob(input)
    assert actual == expected