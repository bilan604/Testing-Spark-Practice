import pytest

from pyspark.sql import SparkSession, Row
from pyspark_test import assert_pyspark_df_equal

from pyspark.sql import DataFrame
from common.spark import inner_join


df_left = spark_session.createDataFrame([
        Row(key=1, name="a"),
        Row(key=2, name="b"),
    ])
df_right = spark_session.createDataFrame([
        Row(key=1, number="001"),
        Row(key=3, number="003"),
    ])
df_expected = spark_session.createDataFrame([
        Row(key=1, name= "a", number="001"),
    ])



@pytest.mark.parametrize("input,expected", 
    [[df_left, df_right, 1]],
    ids=["case 1"])
def test_spark(df_left: DataFrame, df_right: DataFrame, df_expected: DataFrame):
    df_actual = inner_join(df_left, df_right)
    assert df_actual == df_expected