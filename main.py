#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:37:47 2019

@author: Cyan
"""

import pandas as pd
import urllib3  # pip install -i https://pypi.anaconda.org/pypi/simple urllib3
import json
import sys
import warnings

warnings.filterwarnings('ignore')


def data_scraper(competition, type):
    if type == 'public':
        url = 'https://www.kaggle.com/c/{competition}/leaderboard.json?includeBeforeUser=true&includeAfterUser=true'.format(
            competition=competition)
    elif type == 'private':
        url = 'https://www.kaggle.com/c/{competition}/leaderboard.json?includeBeforeUser=true&includeAfterUser=true&type=private'.format(
            competition=competition)
    else:
        print('榜单类型有误，请检查')

    http = urllib3.PoolManager()
    response = http.request('GET', url)
    print('Status Code：' + str(response.status))

    ranks = str(response.data).replace("\\", "")

    return ranks


def data_parser(competition, type='public'):
    ranks0 = data_scraper(competition, type)
    ranks1 = json.loads(ranks0[2:-1])['beforeUser']
    ranks2 = json.loads(ranks0[2:-1])['afterUser']

    ranks = ranks1 + ranks2

    team_list = list(ranks)

    rank_score = pd.DataFrame(columns=['rank', 'teamName', 'entries', 'lastSubmission', 'score'])

    for team in team_list:
        rank = team.get('rank')
        teamName = team.get('teamName')
        entries = team.get('entries')
        lastSubmission = team.get('lastSubmission')
        score = team.get('score')
        rank_score = rank_score.append(
            {'rank': rank, 'teamName': teamName, 'entries': entries, 'lastSubmission': lastSubmission, 'score': score},
            ignore_index=True)

    rank_score = rank_score.dropna()

    return rank_score


if __name__ == "__main__":

    try:
        competition = sys.argv[1]
        type = sys.argv[2]

        print('开始爬取并解析{competition}比赛的leaderboard数据...'.format(competition=competition))
        data = data_parser(competition, type)
        data.to_csv('{competition}_rank_data.csv'.format(competition=competition.replace('-', '_')), index=False)
        print('数据已存入文件...')

    except Exception as e:
        print('输入有误，请检查')
