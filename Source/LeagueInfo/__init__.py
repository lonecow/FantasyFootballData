
from MAFALeagueInfo import MAFALeagueInfo
from SuhNommieNationLeagueInfo import SuhNommieNationLeagueInfo
from FlexLeague import FlexLeague



def CreateFullVarList(NumberOfTeams, ParsedData, LeagueInfo):
    data = []
    starting_counts = LeagueInfo.GetPositionStartingCounts()
    max_counts = LeagueInfo.GetPositionMaxCounts()
    pos_data = LeagueInfo.CreatePosData(ParsedData)
    
    for pos in pos_data:
            data.extend(CreateList(NumberOfTeams, starting_counts[pos], pos_data[pos], NumberOfTeams * max_counts[pos], LeagueInfo.calculatePoints))

    return sorted(data, key=lambda k: k['var'], reverse=True)



""" VAR Average Player"""
def CreateList(NumberOfTeams, NumberOfStartersPerTeam, Players, MaxSizeOfList, calculatePoints):
    data = []

    num_starters = NumberOfStartersPerTeam * NumberOfTeams
    for player in Players:
        data.append({'name':player.name, 'points':calculatePoints(player), 'pos':player.pos, 'team':player.team})
    
    sorted_list = sorted(data, key=lambda k: k['points'], reverse=True)[:MaxSizeOfList]

    ave_starting_player = (sum([x['points'] for x in sorted_list[:num_starters]]) / num_starters)

    for player in sorted_list:
        player['var'] = player['points'] - ave_starting_player

    return sorted_list
    