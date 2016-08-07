'''
Created on Aug 23, 2015

@author: robertbitel
'''

from bs4 import BeautifulSoup
import urllib.request as urllib2

def ConvertTeam(team):
    team_list = {
                        'ARI':'Ari',
                        'ATL':'Atl',
                        'BAL':'Bal',
                        'BUF':'Buf',
                        'CAR':'Car',
                        'CHI':'Chi',
                        'CIN':'Cin',
                        'CLE':'Cle',
                        'DAL':'Dal',
                        'DEN':'Den',
                        'DET':'Det',
                        'FA':'FA',
                        'GB':'GB',
                        'HOU':'Hou',
                        'IND':'Ind',
                        'JAC':'Jac',
                        'LAR':'LA',
                        'KC':'KC',
                        'MIA':'Mia',
                        'MIN':'Min',
                        'NE':'NE',
                        'NO':'NO',
                        'NYG':'NYG',
                        'NYJ':'NYJ',
                        'OAK':'Oak',
                        'PHI':'Phi',
                        'PIT':'Pit',
                        'SD':'SD',
                        'SEA':'Sea',
                        'SF':'SF',
                        'TB':'TB',
                        'TEN':'Ten',
                        'WAS':'Wsh'}
    try:
        return team_list[team]
    except:
        raise Exception('Could not convert Team %s' % (team))

class BaseStatHeader(object):
    def __init__(self, soup, first_level_set_to_check, second_level_set_to_check, HeaderData):
        self._data = HeaderData

        #we are going to check to make sure nothing has changed with how the data is set up
        first_level_header = soup.find('tr', {'class': 'tablehdr'})
        first_level_entries = first_level_header.find_all('td')

        for actual,expected in zip(first_level_entries, first_level_set_to_check):
            if actual.get_text().strip() != expected:
                raise Exception('Header Mismatch Expected: [%s] Actual: [%s]' % (expected, actual.get_text().strip()))


        second_level_header = soup.find('tr', {'class': 'tableclmhdr'})
        second_level_entries = second_level_header.find_all('td')

        for actual,expected in zip(second_level_entries, second_level_set_to_check):
            if actual.get_text().strip().encode('utf8') != expected:
                raise Exception('Header Mismatch Expected: [%s] Actual: [%s]' % (expected, actual.get_text().strip().encode('utf8')))

    def getHeaderInfo(self):
        return self._data


class Player(object):
    def __init__(self, soup, header_info, Position):
        self.stats = {}

        player_elements = soup.find_all('td')
        self.name = player_elements[1].get_text().strip()
        self.team = ConvertTeam(player_elements[2].get_text().strip())
        self.pos = Position
        self.bye = player_elements[3].get_text().strip()

        for element, index in zip(player_elements[4:], range(len(player_elements[4:]))):
            self.stats[header_info.getHeaderInfo()[index]] = element.get_text().strip()

        print(self.name)


class BaseParser(object):
    def __init__(self, Header, Position):
        self._players = []
        self._header = Header
        self._position = Position

    def AddPlayerStats(self, website):
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(website, None, headers)
        response = urllib2.urlopen(req)
        page = response.read() 

        soup = BeautifulSoup(page, 'html.parser')
        header = self._header(soup)

        first_level_header = soup.find('tr', {'class': 'tablehdr'})
        first_level_header.parent
        for item in first_level_header.parent.find_all('tr'):
            if 'class' not in item.attrs:
                self._players.append(Player(item, header, self._position))

    def getPlayers(self):
        return self._players


class QBStatHeader(BaseStatHeader):
    def __init__(self, soup):
        first_level_set_to_check = ['','Passing','Rushing','Fantasy']
        second_level_set_to_check = [   b'Chg',
                                        b'Player\nSort First: \n\n\n\xc2\xa0\xc2\xa0\n\t\tLast:',
                                        b'Team',
                                        b'Bye',
                                        b'Comp',
                                        b'Att',
                                        b'Yard',
                                        b'TD',
                                        b'INT',
                                        b'Att',
                                        b'Yard',
                                        b'TD',
                                        b'FPts']
        HeaderData = [  'COMPLETIONS',
                        'ATTEMPTS',
                        'PASSING_YDS',
                        'PASSING_TD',
                        'PASSING_INT',
                        'RUSHING_RUSH',
                        'RUSHING_YDS',
                        'RUSHING_TD',
                        'FANTASY']

        BaseStatHeader.__init__(self, soup, first_level_set_to_check, second_level_set_to_check, HeaderData)


class RBStatHeader(BaseStatHeader):
    def __init__(self, soup):
        first_level_set_to_check = ['','Rushing','Receiving','Fantasy']
        second_level_set_to_check = [   b'Chg',
                                        b'Player\nSort First: \n\n\n\xc2\xa0\xc2\xa0\n\t\tLast:',
                                        b'Team',
                                        b'Bye',
                                        b'Att',
                                        b'Yard',
                                        b'TD',
                                        b'Rec',
                                        b'Yard',
                                        b'TD',
                                        b'FPts']
        HeaderData = [  'COMPLETIONS',
                        'ATTEMPTS',
                        'RUSHING_RUSH',
                        'RUSHING_YDS',
                        'RUSHING_TD',
                        'RECIEVING_REC',
                        'RECIEVING_YDS',
                        'RECIEVING_TD',
                        'FANTASY']

        BaseStatHeader.__init__(self, soup, first_level_set_to_check, second_level_set_to_check, HeaderData)


class WRStatHeader(BaseStatHeader):
    def __init__(self, soup):
        first_level_set_to_check = ['','Receiving','Rushing','Fantasy']
        second_level_set_to_check = [   b'Chg',
                                        b'Player\nSort First: \n\n\n\xc2\xa0\xc2\xa0\n\t\tLast:',
                                        b'Team',
                                        b'Bye',
                                        b'Rec',
                                        b'Yard',
                                        b'TD',
                                        b'Att',
                                        b'Yard',
                                        b'TD',
                                        b'FPts']
        HeaderData = [  'COMPLETIONS',
                        'ATTEMPTS',
                        'RECIEVING_REC',
                        'RECIEVING_YDS',
                        'RECIEVING_TD',
                        'RUSHING_RUSH',
                        'RUSHING_YDS',
                        'RUSHING_TD',
                        'FANTASY']

        BaseStatHeader.__init__(self, soup, first_level_set_to_check, second_level_set_to_check, HeaderData)


class TEStatHeader(BaseStatHeader):
    def __init__(self, soup):
        first_level_set_to_check = ['','Receiving','Fantasy']
        second_level_set_to_check = [   b'Chg',
                                        b'Player\nSort First: \n\n\n\xc2\xa0\xc2\xa0\n\t\tLast:',
                                        b'Team',
                                        b'Bye',
                                        b'Rec',
                                        b'Yard',
                                        b'TD',
                                        b'FPts']
        HeaderData = [  'COMPLETIONS',
                        'ATTEMPTS',
                        'RECIEVING_REC',
                        'RECIEVING_YDS',
                        'RECIEVING_TD',
                        'FANTASY']

        BaseStatHeader.__init__(self, soup, first_level_set_to_check, second_level_set_to_check, HeaderData)


class DEFStatHeader(BaseStatHeader):
    def __init__(self, soup):
        first_level_set_to_check = ['','','Fantasy']
        second_level_set_to_check = [   b'Chg',
                                        b'Player\nSort First: \n\n\n\xc2\xa0\xc2\xa0\n\t\tLast:',
                                        b'Team',
                                        b'Bye',
                                        b'Tackle',
                                        b'Assist',
                                        b'Sack',
                                        b'PD',
                                        b'INT',
                                        b'FF',
                                        b'FR',
                                        b'FPts']

        HeaderData = [  'TACKLES',
                        'ASSIST',
                        'SACKS',
                        'PASSESDEFENSED',
                        'INTERCEPTIONS',
                        'FUMBLESFORCED',
                        'FUMBLESRECOVERED',
                        'FANTASY']

        BaseStatHeader.__init__(self, soup, first_level_set_to_check, second_level_set_to_check, HeaderData)


class QBParser(BaseParser):
    def __init__(self):
        BaseParser.__init__(self, QBStatHeader, 'QB')


class RBParser(BaseParser):
    def __init__(self):
        BaseParser.__init__(self, RBStatHeader, 'RB')


class WRParser(BaseParser):
    def __init__(self):
        BaseParser.__init__(self, WRStatHeader, 'WR')


class TEParser(BaseParser):
    def __init__(self):
        BaseParser.__init__(self, TEStatHeader, 'TE')


class DLParser(BaseParser):
    def __init__(self):
        BaseParser.__init__(self, DEFStatHeader, 'DL')


class LBParser(BaseParser):
    def __init__(self):
        BaseParser.__init__(self, DEFStatHeader, 'LB')


class DBParser(BaseParser):
    def __init__(self):
        BaseParser.__init__(self, DEFStatHeader, 'DB')


if __name__ == '__main__':
    import os

    path = 'file:///%s' % (os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'Tests', 'EspnParserTest','TestData', 'FFTodayQB_2016.html')))
    print(path)
    TestClass = QBParser()
    TestClass.AddPlayerStats(path)
    #TestClass.AddPlayerStats(path2)
