import pytest

from pyspark.sql import SparkSession, Row
from pyspark_test import assert_pyspark_df_equal

from common.spark import inner_join

# fix test cases
@pytest.mark.parametrize("input,expected", 
    [["1", 1],
    ["4", 4]],
    ids=["case 1", "case 2"])
def test_parse(input: str, expected: int):
    actual = inner_join(input)
    assert actual == expected