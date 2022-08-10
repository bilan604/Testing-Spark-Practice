from __future__ import annotations

from pyspark.sql import DataFrame


def inner_join(df_left: DataFrame, df_right: DataFrame) -> DataFrame:
    return df_left.join(df_right, on=["key"], how="inner")