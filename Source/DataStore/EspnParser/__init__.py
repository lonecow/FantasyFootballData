
from .EspnParser import EspnParser
from .EspnKickerParser import EspnKickerParser
from .DefenseParser import DefenseParser

class EspnData(object):
    def __init__(self):

        self.quarter_backs = []
        self.widerecievers = []
        self.runningbacks = []
        self.tightends = []

        positions = [   ('QB', self.quarter_backs),
                        ('WR', self.widerecievers),
                        ('TE', self.tightends),
                        ('RB', self.runningbacks)]
        base_parser = EspnParser()

        categories = [0, 2, 4, 6]
        for category in categories:
            for index in range(0, 300, 40):
                website = 'http://games.espn.com/ffl/tools/projections?&slotCategoryId=%s&startIndex=%s' % (category, index)
                if EspnParser.PageHasPlayers(website):
                    base_parser.AddPlayerStats(website)
                elif index == 0:
                    raise Exception('Something is wrong with the website. Pattern might have changed')

        for player in base_parser.getPlayers():
            found = False
            for pos_name, pos_list in positions:
                if player.pos == pos_name:
                    pos_list.append(player)
                    found = True

            if not found:
                raise Exception('Could Not find Position [%s]' % player.pos)


        kicker_parser = EspnKickerParser()
        kicker_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?display=alt&slotCategoryId=17')
        kicker_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?display=alt&slotCategoryId=17&startIndex=15')
        self.kickers = kicker_parser.getPlayers()

        #defense_parser = DefenseParser()
        #defense_parser.AddPlayerStats('http://www.fantasysharks.com/apps/bert/forecasts/projections.php?League=&Position=98&scoring=1&Segment=522&uid=4')
        #self.defense = defense_parser.getPlayers()