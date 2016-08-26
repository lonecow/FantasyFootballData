'''
Created on Aug 23, 2015

@author: robertbitel
'''

class BaseLeagueInfo(object):
    '''
    classdocs
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

    def GetLeaguePlayerOweners(self):
        return []

    def GetPositionDictionary(self, data):
        return {}

    def CreatePosData(self, data):
        '''
        @type data : Espnparser.EspnData
        '''
        def FindOwner(PlayerToFind, OwnerList):
            found_player = None
            for owner_player in OwnerList:
                if owner_player == PlayerToFind:
                    found_player = owner_player
                    break;

            return found_player

        owners_list = self.GetLeaguePlayerOweners()

        for player in data.quarter_backs + data.runningbacks + data.widerecievers + data.tightends + data.kickers + data.defense:
            owner = FindOwner(player, owners_list)
            if owner is None:
                player.owner = 'FA'
            else:
                player.owner = owner.owner

        return self.GetPositionDictionary(data)
