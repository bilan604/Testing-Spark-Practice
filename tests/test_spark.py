import pytest

from pyspark.sql import SparkSession, Row
from pyspark_test import assert_pyspark_df_equal

from pyspark.sql import DataFrame
from common.functions.hello_spark import inner_join



# currently incompatible with test_join function

@pytest.mark.parametrize("input1, input2, expected", 
    [[df_left, df_right, 1]],
    ids=["case 1"])
def test_inner_join(df_left: DataFrame, df_right: DataFrame, df_expected: DataFrame):
    df_actual = inner_join(df_left, df_right)
    assert df_actual == df_expected