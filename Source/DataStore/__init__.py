
def GetPlayerData():
    def FindPlayer(PlayerList, PlayerToFind):
        found_player = None
        for player in PlayerList:
            if player == PlayerToFind:
                found_player = player
                break;

        return found_player

    def GetAllPlayerList(DataParser):
        pos_list = [    'quarter_backs',
                        'widerecievers',
                        'runningbacks',
                        'tightends',
                        'kickers',
                        'defense']
        all_DataParser = []
        for pos in pos_list:
            if pos in dir(DataParser):
                all_DataParser.extend(eval('DataParser.%s' %(pos)))
        return all_DataParser

    from .EspnParser import EspnData
    from .FFTodayParser import FFTodayData
    print('Downloading Espn Data')
    espn_data = EspnData()
    print('Downloading FFToday Data')
    ff_today_data = FFTodayData()

    print('Averaging Scores')

    # we are going to use kickers from espn
    ff_today_data.kickers = espn_data.kickers
    # we are going to use defense from ff_today
    espn_data.defense = ff_today_data.defense

    source_1 = espn_data
    source_2 = ff_today_data

    list1 = GetAllPlayerList(source_1)
    list2 = GetAllPlayerList(source_2)

    for player in list1:
        found_player = FindPlayer(list2, player)
        if found_player != None:
            for stat in player.stats:
                if stat in found_player.stats:
                    player.stats[stat] = (player.stats[stat] + found_player.stats[stat]) / 2
        else:
            #print('Could Not Find Player [%s]' % (player.name))
            pass

    return source_1