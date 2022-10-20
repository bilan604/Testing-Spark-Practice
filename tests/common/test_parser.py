import pytest

from tests.common.parser import Parser

@pytest.mark.parametrize("input,expected", 
    [["1", 1],
    ["2", 2],
    ["3", 3],
    ["4", 4]],
    ids=["case 1", "case 2", "case 3", "case 4"])
def test_parse(input: str, expected: int):
    actual = Parser.str_to_int(input)
    assert actual == expected

print("Done")