import numpy as np
import pandas as pd

from bs4 import BeautifulSoup

from typing import *
from __future__ import annotations

# the bot
from review_bot import GlassdoorReviewScrapper

# from JSON format to a pandas DataFrame
def JSON_to_DataFrame(json_data: dict):
    dd_ret = {'rater': [], 'pros': [], 'cons': [], 'rating': []}
    for key in json_data:
        if type(key) == int:
            for inner_key in json_data[key]:
                dd_ret[inner_key].append(json_data[key][inner_key])
    return pd.DataFrame(dd_ret)

# creates a python dictionary that can be directly turned into a pandas dataframe
def as_dd(json_data: dict):
    dd_ret = {'rater': [], 'pros': [], 'cons': [], 'rating': []}
    for key in json_data:
        if type(key) == int:
            for inner_key in json_data[key]:
                dd_ret[inner_key].append(json_data[key][inner_key])
    return dd_ret

# creates a DataFrame; outdated
def as_DataFrame(rater, pros, cons, rating):
    dd_df = {"rater": rater, "pros": pros, "cons": cons, "rating": rating}
    return pd.DataFrame(dd_df)