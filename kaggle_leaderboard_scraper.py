#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:37:47 2019

@author: Cyan
"""

import pandas as pd
import urllib3 #  pip install -i https://pypi.anaconda.org/pypi/simple urllib3
import unicodedata
import requests
import datetime
import xlsxwriter
from bs4 import BeautifulSoup, SoupStrainer, Comment
import json
import warnings
warnings.filterwarnings('ignore')
description_list = []
url_list = []
status_list = []
datetime_list = []

url='https://www.kaggle.com/c/ieee-fraud-detection/leaderboard.json?includeBeforeUser=true&includeAfterUser=true&type=private'

http = urllib3.PoolManager()
response = http.request('GET',url)
print('Status Code：' + str(response.status))

ranks0 = str(response.data).replace("\\", "")


ranks1 = json.loads(ranks0[2:-1])['beforeUser']
ranks2 = json.loads(ranks0[2:-1])['afterUser']

ranks = ranks1 + ranks2

team_list = list(ranks)

rank_score = pd.DataFrame(columns = ['rank', 'score'])

for team in team_list:
    rank = team.get('rank')
    score = team.get('score')
    rank_score = rank_score.append({'rank': rank, 'score': score}, ignore_index=True)

rank_score = rank_score.dropna()





