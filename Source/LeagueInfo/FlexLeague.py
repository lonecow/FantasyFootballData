'''
Created on Aug 23, 2015

@author: robertbitel
'''

from BaseLeagueInfo import BaseLeagueInfo

class FlexLeague(BaseLeagueInfo):
    '''
    classdocs
    '''


    _points_ary = [
                    ('COMPLETIONS',      0),
                    ('ATTEMPTS',         0),
                    ('PASSING_YDS',      0.05),
                    ('PASSING_TD',       7),
                    ('PASSING_INT',      -2),
                    ('RUSHING_RUSH',     0),
                    ('RUSHING_YDS',      0.2),
                    ('RUSHING_TD',       10),
                    ('RECIEVING_REC',    2),
                    ('RECIEVING_YDS',    0.2),
                    ('RECIEVING_TD',     10),
                    ('SCORED_1-39,',     0),
                    ('ATTEMPTED_1-39,',  0),
                    ('SCORED_40-49,',    0),
                    ('ATTEMPTED_40-49,', 0),
                    ('SCORED_50+',       0),
                    ('ATTEMPTED_50+',    0),
                    ('SCORED_TOT',       0),
                    ('ATTEMPTED_TOT',    0),
                    ('SCORED_XP',        0),
                    ('ATTEMPTED_XP',     0),
                    ('TACKLES',          0),
                    ('ASSIST',           0),
                    ('SACKS',            0),
                    ('PASSESDEFENSED',   0),
                    ('INTERCEPTIONS',    0),
                    ('FUMBLESRECOVERED', 0),
                    ('FUMBLESFORCED',    0),
                    ('DEFENSEIVETDS',   0)]

    _starting_positions = {'FLEX':7, 'OP':2}
    _max_positions = {'FLEX':12, 'OP':4}


    def __init__(self):
        super(BaseLeagueInfo, self).__init__()

    def CreatePosData(self, data):
        flex = []
        flex.extend(data.runningbacks)
        flex.extend(data.widerecievers)
        flex.extend(data.tightends)
        return {'FLEX':flex, 'OP':data.quarter_backs} 
