import pytest
from commonFunctions.count_and_say import CountAndSay

@pytest.mark.parametrize("input,expected", 
    [[1, "1"],
    [4, "1211"],
    [8,"1113213211"],
    [12,"3113112221232112111312211312113211"]],
    ids=["case 1", "case 2", 'case 3', 'case 4'])
def test_say(input: int, expected: str):
    actual = CountAndSay.say(input)
    assert actual == expected
