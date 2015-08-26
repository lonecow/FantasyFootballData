'''
Created on Aug 23, 2015

@author: robertbitel
'''

from BaseLeagueInfo import BaseLeagueInfo

from CurrentRosterParser import CurrentRosterParser

class SuhNommieNationLeagueInfo(BaseLeagueInfo):
    '''
    classdocs
    '''


    _points_ary = [
                    ('COMPLETIONS',      2), #this is 2 because we already minus 1 for the attempt but if it was complete it should be +1
                    ('ATTEMPTS',         -1),
                    ('PASSING_YDS',      0.04),
                    ('PASSING_TD',       10),
                    ('PASSING_INT',      -5),
                    ('RUSHING_RUSH',     0.2),
                    ('RUSHING_YDS',      0.2),
                    ('RUSHING_TD',       10),
                    ('RECIEVING_REC',    1),
                    ('RECIEVING_YDS',    0.2),
                    ('RECIEVING_TD',     10),
                    ('SCORED_1-39,',     8), # this is 8 because we already minus 4 for the attempt
                    ('ATTEMPTED_1-39,',  -4),
                    ('SCORED_40-49,',    9), # this is 9 because we already minus 3 for the attempt
                    ('ATTEMPTED_40-49,', -3),
                    ('SCORED_50+',       10), # this is 10 because we already minus 2 for the attempt
                    ('ATTEMPTED_50+',    -2),
                    ('SCORED_TOT',       0),
                    ('ATTEMPTED_TOT',    0),
                    ('SCORED_XP',        4), # this is 4 because we already minus 2 for the attempt
                    ('ATTEMPTED_XP',     -2),
                    ('TACKLES',         0.2),
                    ('ASSIST',          1),
                    ('SACKS',           5),
                    ('PASSESDEFENSED',  2),
                    ('INTERCEPTIONS',   5),
                    ('FUMBLESRECOVERED',5),
                    ('FUMBLESFORCED',   5),
                    ('DEFENSEIVETDS',   10)]

    _starting_positions = {'QB':2, 'RB':2, 'WR':3, 'TE':1, 'K':1, 'D':3}
    _max_positions = {'QB':4, 'RB':5, 'WR':6, 'TE':3, 'K':2, 'D':5}


    def __init__(self):
        super(BaseLeagueInfo, self).__init__()

    def CreatePosData(self, data):
        '''
        @type data : Espnparser.EspnData
        '''
        return {'QB': data.quarter_backs, 'RB':data.runningbacks, 'WR':data.widerecievers, 'TE':data.tightends, 'K':data.kickers, 'D':data.defense}

    def GetLeaguePlayerOweners(self):
        import os
        import urllib
        import urlparse
        def path2url(path):
            return urlparse.urljoin(
            'file:', urllib.pathname2url(path))

        path = path2url(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'PlayerData.txt'))
        TestClass = CurrentRosterParser()
        TestClass.AddPlayerStats(path)

        return TestClass.getPlayers()

