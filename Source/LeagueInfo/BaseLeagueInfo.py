'''
Created on Aug 23, 2015

@author: robertbitel
'''

class BaseLeagueInfo(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        

    def calculatePoints(self, player):
        points = 0.0

        for (stat, multiplier) in self._points_ary:
            try:
                points += float(player.stats[stat]) * float(multiplier)
            except:
                pass
        return points


    def GetPositionStartingCounts(self):
        return self._starting_positions


    def GetPositionMaxCounts(self):
        return self._max_positions