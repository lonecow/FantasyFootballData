'''
Created on Aug 23, 2015

@author: robertbitel
'''
from bs4 import BeautifulSoup
try:
    import urllib2  # @UnresolvedImport @UnusedImport
except:
    import urllib.request as urllib2  # @Reimport

class EspnKickerStatHeader(object):
    def __init__(self, soup):
        '''for now we are just going to hard code it. If we have time we will get this later'''
        self._data = [  'SACKS',
                        'INTERCEPTIONS',
                        'FUMBLESRECOVERED',
                        'DEFENSEIVETDS',
                        'POINTSAGAINST',
                        'YARDSAGAINST']

    def getHeaderInfo(self):
        return self._data

class EspnKickerPlayer(object):
    def __init__(self, soup, header_info):
        self.stats = {}

        player_name_item = soup.find_all('span', {'class': 'subheadPlayerNameLink'})[0]
        self.name = player_name_item.a.string
        self.team = []
        self.pos = 'DT'
        print('Defense Team %s' % (self.name))

        for item in soup.find_all('tr', {'class': 'tableBody'}):
            if item.td.string == '2017 Projections':
                proj_item = item
        
        player_stat_list = proj_item.find_all('td', {'class': 'playertableStat'})
        for count in range(len(header_info.getHeaderInfo())):
            self.stats[header_info.getHeaderInfo()[count]] = player_stat_list[count].string

        for item in self.stats:
            if self.stats[item] == '--':
                self.stats[item] = float(0.0)
            else:
                self.stats[item] = float(self.stats[item])

class DefenseTeamParser(object):
    def __init__(self):
        self._players = []

    def AddPlayerStats(self, website):
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(website, None, headers)
        response = urllib2.urlopen(req)
        page = response.read() 

        soup = BeautifulSoup(page, 'html.parser')
        header = EspnKickerStatHeader(soup)
        for item in soup.find_all('table', {'class': 'tableBody'}):
            self._players.append(EspnKickerPlayer(item, header))
            pass
    
    def getPlayers(self):
        return self._players

if __name__ == '__main__':
    test = DefenseTeamParser()
    test.AddPlayerStats('http://games.espn.com/ffl/tools/projections?display=alt&slotCategoryId=16')