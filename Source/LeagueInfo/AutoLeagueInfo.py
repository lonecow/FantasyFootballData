'''
Created on Aug 23, 2015

@author: robertbitel
'''

from .BaseLeagueInfo import BaseLeagueInfo

class AutoLeagueInfo(BaseLeagueInfo):
    '''
    classdocs
    '''

    _points_ary = [
                    ('COMPLETIONS',      0),
                    ('ATTEMPTS',         0),
                    ('PASSING_YDS',      float(1/25)),
                    ('PASSING_TD',       4),
                    ('PASSING_INT',      -1),
                    ('RUSHING_RUSH',     0),
                    ('RUSHING_YDS',      float(1/10)),
                    ('RUSHING_TD',       6),
                    ('RECIEVING_REC',    float(0.2)),
                    ('RECIEVING_YDS',    float(1/10)),
                    ('RECIEVING_TD',     6),
                    ('SCORED_1-39,',     3),
                    ('ATTEMPTED_1-39,',  0),
                    ('SCORED_40-49,',    4),
                    ('ATTEMPTED_40-49,', 0),
                    ('SCORED_50+',       5),
                    ('ATTEMPTED_50+',    0),
                    ('SCORED_TOT',       0),
                    ('ATTEMPTED_TOT',    0),
                    ('SCORED_XP',        1),
                    ('ATTEMPTED_XP',     0),
                    ('TACKLES',         0),
                    ('ASSIST',          0),
                    ('SACKS',           1),
                    ('PASSESDEFENSED',  0),
                    ('INTERCEPTIONS',   2),
                    ('FUMBLESRECOVERED',2),
                    ('FUMBLESFORCED',   0),
                    ('DEFENSEIVETDS',   6),
                    ('POINTSAGAINST',   float(-1/21)),
                    ('YARDSAGAINST',    0)]

    _starting_positions = {'QB':1, 'RB':2, 'WR':2, 'TE':1, 'K':1, 'DT':1}
    _max_positions = {'QB':3, 'RB':5, 'WR':5, 'TE':3, 'K':2, 'DT':2}

    def __init__(self):
        pass

    def GetPositionDictionary(self, data):
        return {    'QB': data.quarter_backs,
                    'RB':data.runningbacks,
                    'WR':data.widerecievers,
                    'TE':data.tightends,
                    'K':data.kickers,
                    'DT':data.defenseteam}

    def GetLeaguePlayerOweners(self):
        return []
