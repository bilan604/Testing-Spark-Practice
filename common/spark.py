from __future__ import annotations

from pyspark.sql import DataFrame


def inner_join(df_left: DataFrame, df_right: DataFrame) -> DataFrame:
    return df_left.join(df_right, on=["key"], how="inner")


def left_join(df_left: DataFrame, df_right: DataFrame) -> DataFrame:
    return df_left.join(df_right, on=["key"], how="left")


def right_join(df_left: DataFrame, df_right: DataFrame) -> DataFrame:
    return df_left.join(df_right, on=["key"], how="right")


def outer_join(df_left: DataFrame, df_right: DataFrame) -> DataFrame:
    return df_left.join(df_right, on=["key"], how="outer")

