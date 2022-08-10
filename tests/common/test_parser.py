import pytest

from common.parser import Parser

@pytest.mark.parametrize("input,expected", 
    [["1", 1],
    ["4", 4]],
    ids=["case 1", "case 2"])
def test_parse(input: str, expected: int):
    actual = Parser.parse(input)
    assert actual == expected
