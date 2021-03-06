'''
Created on Aug 22, 2015

@author: robertbitel
'''
import DataStore

from LeagueInfo import MAFALeagueInfo, MAFALeagueInfo_Playoffs, SuhNommieNationLeagueInfo, FlexLeague, AutoLeagueInfo, CreateFullVarList, CreateFullOwnerList
from FileWriter import WriteByPosition, WriteFullList_NoOwner, WriteFullList_Owner

if __name__ == '__main__':
    data = DataStore.GetPlayerData()

    mafa_10_league = CreateFullVarList(10, data, MAFALeagueInfo())
    mafa_12_league = CreateFullVarList(12, data, MAFALeagueInfo())
    mafa_14_league = CreateFullVarList(14, data, MAFALeagueInfo())
    mafa_14_playoff_league = CreateFullVarList(14, data, MAFALeagueInfo_Playoffs())
    snn_12_league = CreateFullVarList(12, data, SuhNommieNationLeagueInfo())
    snn_12_league_myteam = CreateFullOwnerList('Strk', 12, data, SuhNommieNationLeagueInfo())
    flex_10_league = CreateFullVarList(10, data, FlexLeague())
    flex_12_league = CreateFullVarList(12, data, FlexLeague())
    AutoLeague_league = CreateFullVarList(12, data, AutoLeagueInfo())


    files_to_write = [  (mafa_10_league, './MAFA_10_VAR_List.csv',  WriteByPosition),
                        (mafa_12_league, './MAFA_12_VAR_List.csv',  WriteByPosition),
                        (mafa_14_league, './MAFA_14_VAR_List.csv',  WriteByPosition),
                        (mafa_14_playoff_league, './MAFA_14_VAR_PLAYOFF_List.csv',  WriteByPosition),
                        (mafa_14_league, './MAFA_14_VAR_Full_List.csv',  WriteFullList_NoOwner),
                        (snn_12_league, './SNN_12_VAR_List.csv',    WriteByPosition),
                        (snn_12_league, './SNN_12_VAR_Full_List.csv',    WriteFullList_Owner),
                        (AutoLeague_league, './AL_12_VAR_List.csv',    WriteByPosition),
                        (snn_12_league_myteam, './SNN_12_VAR_Full_List_MyTeam.csv',    WriteFullList_Owner),
                        (flex_10_league, './FLEX_10_VAR_List.csv',  WriteFullList_NoOwner),
                        (flex_12_league, './FLEX_12_VAR_List.csv',  WriteFullList_NoOwner)]


    for (data, file_name, write_func) in files_to_write:
        write_func(data, file_name)


