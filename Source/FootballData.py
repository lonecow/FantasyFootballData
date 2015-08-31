'''
Created on Aug 22, 2015

@author: robertbitel
'''

from EspnParser import EspnData

from LeagueInfo import MAFALeagueInfo, SuhNommieNationLeagueInfo, FlexLeague, CreateFullVarList
from FileWriter import WriteByPosition, WriteFullList

if __name__ == '__main__':
    data = EspnData()

    mafa_12_league = CreateFullVarList(12, data, MAFALeagueInfo())
    mafa_14_league = CreateFullVarList(14, data, MAFALeagueInfo())
    snn_12_league = CreateFullVarList(12, data, SuhNommieNationLeagueInfo())
    flex_10_league = CreateFullVarList(10, data, FlexLeague())


    files_to_write = [  (mafa_12_league, './MAFA_12_VAR_List.csv',  WriteByPosition),
                        (mafa_14_league, './MAFA_14_VAR_List.csv',  WriteByPosition),
                        (snn_12_league, './SNN_12_VAR_List.csv',    WriteByPosition),
                        (flex_10_league, './FLEX_10_VAR_List.csv',  WriteFullList)]


    for (data, file_name, write_func) in files_to_write:
        write_func(data, file_name)

    