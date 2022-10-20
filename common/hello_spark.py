
import logging
from logging.config import fileConfig
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession, Row
from pyspark_test import assert_pyspark_df_equal

from __future__ import annotations

from functions.parser import Parser
from functions.test_join_dfs import *


fileConfig('logging.ini')
logger = logging.getLogger(__name__)


def main():
    logger.info("Hello world")


if __name__ == "__main__":
    main()