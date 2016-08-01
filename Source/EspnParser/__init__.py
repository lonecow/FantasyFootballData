
from .EspnParser import EspnParser
from .EspnKickerParser import EspnKickerParser
from .DefenseParser import DefenseParser

class EspnData(object):
    def __init__(self):
        quarterback_parser = EspnParser()
        quarterback_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?slotCategoryId=0')
        quarterback_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?slotCategoryId=0&startIndex=40')
        self.quarter_backs = quarterback_parser.getPlayers()

        runningback_parser = EspnParser()
        runningback_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?slotCategoryId=2')
        runningback_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?slotCategoryId=2&startIndex=40')
        self.runningbacks = runningback_parser.getPlayers()

        widereciever_parser = EspnParser()
        widereciever_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?slotCategoryId=4')
        widereciever_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?slotCategoryId=4&startIndex=40')
        self.widerecievers = widereciever_parser.getPlayers()

        tightend_parser = EspnParser()
        tightend_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?slotCategoryId=6')
        tightend_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?slotCategoryId=6&startIndex=40')
        self.tightends = tightend_parser.getPlayers()

        kicker_parser = EspnKickerParser()
        kicker_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?display=alt&slotCategoryId=17')
        kicker_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?display=alt&slotCategoryId=17&startIndex=15')
        self.kickers = kicker_parser.getPlayers()

        defense_parser = DefenseParser()
        defense_parser.AddPlayerStats('http://www.fantasysharks.com/apps/bert/forecasts/projections.php?League=&Position=98&scoring=1&Segment=522&uid=4')
        self.defense = defense_parser.getPlayers()