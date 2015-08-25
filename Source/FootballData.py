'''
Created on Aug 22, 2015

@author: robertbitel
'''

from EspnParser import EspnData

from LeagueInfo import MAFALeagueInfo, SuhNommieNationLeagueInfo, FlexLeague, CreateFullVarList

if __name__ == '__main__':
    data = EspnData()

    mafa_12_league = CreateFullVarList(12, data, MAFALeagueInfo())
    mafa_14_league = CreateFullVarList(14, data, MAFALeagueInfo())
    snn_12_league = CreateFullVarList(12, data, SuhNommieNationLeagueInfo())
    flex_10_league = CreateFullVarList(10, data, FlexLeague())


    files_to_write = [  (mafa_12_league, './MAFA_12_VAR_List.csv'),
                        (mafa_14_league, './MAFA_14_VAR_List.csv'),
                        (snn_12_league, './SNN_12_VAR_List.csv'),
                        (flex_10_league, './FLEX_10_VAR_List.csv')]


    for (data, file_name) in files_to_write:
        fd = open(file_name, 'w')

        fd.write('Player,Position,Team,Var\n')
        for item in data:
            fd.write('%s,%s,%s,%.4f\n' % (item['name'], item['pos'], item['team'], item['var']))

        fd.close()

    