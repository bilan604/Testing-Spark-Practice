from data_conversion import *
from review_bot import GlassdoorReviewScrapper
import re
from time
import requests
import BeautifulSoup


grs = GlassdoorReviewScrapper('https://www.glassdoor.com/Reviews/SynergisticIT-Reviews-E424823.htm?filter.iso3Language=eng')
grs.scrape()

# creating a pandas DataFrame of reviews
df = JSON_to_DataFrame(grs.JSON_data)