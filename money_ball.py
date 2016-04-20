from data import *
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt






main = pd.read_csv('data/Master.csv', dtype='str')

main = main[['playerID', 'nameFirst', 'nameLast', 'finalGame']].copy()

batting = pd.read_csv('data/Batting.csv', dtype='str')

batting = batting[['playerID', 'yearID', 'AB', 'R', 'H', 'HR', 'RBI', 'BB', 'HBP', 'SF']].copy()

salaries = pd.read_csv('data/Salaries.csv', dtype='str')

salaries = salaries[['yearID', 'teamID', 'playerID', 'salary']].copy()

fielding = pd.read_csv('data/Fielding.csv', dtype='str')

fielding = fielding[['playerID', 'yearID', 'POS', 'G']].copy()

test = pd.merge(pd.merge(main, salaries), batting)

stats = pd.merge(test, fielding)

stats['H'] = stats['H'].astype(float)


stats['BB'] = stats['BB'].astype(float)


stats['HBP'] = stats['HBP'].astype(float)


stats['AB'] = stats['AB'].astype(float)


stats['SF'] = stats['SF'].astype(float)

stats['G'] = stats['G'].astype(float)

stats['OBP'] = ((stats.H) + (stats.BB) + (stats.HBP))/((stats.AB) + (stats.BB) + (stats.HBP) + (stats.SF))

stats = (stats[(stats.AB > 30)].sort_values(by='OBP', ascending=False))
stats = (stats[(stats.G > 20)].sort_values(by='OBP', ascending=False))
stats = (stats[(stats.POS != 'OF')].sort_values(by='OBP', ascending=False))
stats = stats.loc[stats['yearID'] == '1988']


top_position = {'1B': '', '2B': '', '3B': '', 'LF': '', 'CF': '', 'RF': '', 'SS': '', 'C': '', 'P': ''}

for pos in top_position:
    stat_pos = (stats[(stats.POS == pos)].sort_values(by='OBP', ascending=False))
    top_position_OBP = stat_pos.OBP.max()
    stat_pos = (stat_pos[(stat_pos.OBP == top_position_OBP)].sort_values(by='HR', ascending=False))
    top_position_HR = stat_pos.HR.max()
    stat_pos = (stat_pos[(stat_pos.HR == top_position_HR)].sort_values(by='HR', ascending=False))
    top_position[pos] = [(stat_pos.nameLast), (stat_pos.salary)]

#     top_position[pos] = [player_info.nameLast, player_info.salary]
#
print(top_position)


# for year in range(1985, 2016)


# print(stats[(stats.AB > 100)].sort_values(by='yearID', ascending=False))

# print(stats[(stats.OBP > .5) & (stats.OBP < 1)].sort_values(by='OBP', ascending=False))
