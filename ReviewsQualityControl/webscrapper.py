#%%
import os
import re
import time
import math
import random
import statistics
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from timeit import default_timer
from numpy import unique, ravel
from numpy import sqrt, dot, array, diagonal, mean, transpose, eye, diag, ones
from numpy import transpose, diag, dot
from numpy.linalg import svd, inv, qr, det
from sklearn.linear_model import LinearRegression
from matplotlib.pyplot import figure
import seaborn as sns

#%%
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

#%%
class CompanyReviewScrapper(object):

    def __init__(self, company_name):
        self.company_name = company_name
        self.reviews = {}  # dict of dicts



# %%
