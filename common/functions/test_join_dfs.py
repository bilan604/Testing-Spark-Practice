import pytest

from pyspark.sql import SparkSession, Row
from pyspark_test import assert_pyspark_df_equal


from hello_spark import inner_join, left_join, right_join, outer_join


def test_join(spark_session: SparkSession):
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

    # When
    df_actual = inner_join(df_left=df_left, df_right=df_right)

    # Then
    assert_pyspark_df_equal(df_actual, df_expected)