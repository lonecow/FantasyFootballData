
from .EspnParser import EspnParser
from .EspnKickerParser import EspnKickerParser
from .DefenseParser import DefenseParser
from .DefenseTeamParser import DefenseTeamParser

class EspnData(object):
    def __init__(self):

        self.quarter_backs = []
        self.widerecievers = []
        self.runningbacks = []
        self.tightends = []

        positions = [   ('QB', self.quarter_backs),
                        ('WR', self.widerecievers),
                        ('TE', self.tightends),
                        ('RB', self.runningbacks),
                        ('RB, EDR', self.runningbacks)]
        base_parser = EspnParser()

        categories = [0, 2, 4, 6]
        for category in categories:
            for index in range(0, 300, 40):
                website = 'http://games.espn.com/ffl/tools/projections?&slotCategoryId=%s&startIndex=%s' % (category, index)
                print('Reading Website [%s]' % (website))
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
                raise Exception('Could Not find Position [%s] [%s]' % (player.pos, player.name))


        kicker_parser = EspnKickerParser()
        kicker_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?display=alt&slotCategoryId=17')
        kicker_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?display=alt&slotCategoryId=17&startIndex=15')
        self.kickers = kicker_parser.getPlayers()


        dt_parser = DefenseTeamParser()
        dt_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?display=alt&slotCategoryId=16')
        dt_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?display=alt&slotCategoryId=16&startIndex=15')
        dt_parser.AddPlayerStats('http://games.espn.go.com/ffl/tools/projections?display=alt&slotCategoryId=16&startIndex=30')
        self.defenseteam = dt_parser.getPlayers()

        #defense_parser = DefenseParser()
        #defense_parser.AddPlayerStats('http://www.fantasysharks.com/apps/bert/forecasts/projections.php?League=&Position=98&scoring=1&Segment=522&uid=4')
        #self.defense = defense_parser.getPlayers()