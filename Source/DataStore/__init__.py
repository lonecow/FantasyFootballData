
def GetPlayerData():
    def FindPlayer(PlayerList, Name):
        found_player = None
        for player in PlayerList:
            if player.name == Name:
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

    all_espn_data = GetAllPlayerList(espn_data)
    all_ff_today_data = GetAllPlayerList(ff_today_data)

    for player in all_espn_data:
        ff_today_player = FindPlayer(all_ff_today_data, player.name)
        if ff_today_player != None:
            for stat in player.stats:
                if stat in ff_today_player.stats:
                    player.stats[stat] = (player.stats[stat] + ff_today_player.stats[stat]) / 2
        else:
            print('Could Not Find Player [%s]' % (player.name))

    return espn_data