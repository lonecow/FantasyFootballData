'''
Created on Aug 23, 2015

@author: robertbitel
'''

from BaseLeagueInfo import BaseLeagueInfo

class MAFALeagueInfo(BaseLeagueInfo):
    '''
    classdocs
    '''

    _points_ary = [
                    ('COMPLETIONS',      0),
                    ('ATTEMPTS',         0),
                    ('PASSING_YDS',      1),
                    ('PASSING_TD',       50),
                    ('PASSING_INT',      -50),
                    ('RUSHING_RUSH',     0),
                    ('RUSHING_YDS',      1),
                    ('RUSHING_TD',       50),
                    ('RECIEVING_REC',    0),
                    ('RECIEVING_YDS',    1),
                    ('RECIEVING_TD',     50),
                    ('SCORED_1-39,',     25),
                    ('ATTEMPTED_1-39,',  0),
                    ('SCORED_40-49,',    55),
                    ('ATTEMPTED_40-49,', 0),
                    ('SCORED_50+',       55),
                    ('ATTEMPTED_50+',    0),
                    ('SCORED_TOT',       0),
                    ('ATTEMPTED_TOT',    0),
                    ('SCORED_XP',        10),
                    ('ATTEMPTED_XP',     0),
                    ('TACKLES',         10),
                    ('ASSIST',          5),
                    ('SACKS',           50),
                    ('PASSESDEFENSED',  0),
                    ('INTERCEPTIONS',   50),
                    ('FUMBLESRECOVERED',0),
                    ('FUMBLESFORCED',   0),
                    ('DEFENSEIVETDS',   50)]

    _starting_positions = {'QB':1, 'RB':2, 'WR':2, 'TE':1, 'K':1, 'D':3}
    _max_positions = {'QB':3, 'RB':5, 'WR':5, 'TE':3, 'K':2, 'D':5}

    def __init__(self):
        super(BaseLeagueInfo, self).__init__()

    def CreatePosData(self, data):
        return {'QB': data.quarter_backs, 'RB':data.runningbacks, 'WR':data.widerecievers, 'TE':data.tightends, 'K':data.kickers, 'D':data.defense}


    def GetLeaguePlayerOweners(self):
        return []
