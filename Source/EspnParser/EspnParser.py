'''
Created on Aug 23, 2015

@author: robertbitel
'''

from bs4 import BeautifulSoup
try:
    import urllib2
except:
    import urllib.request as urllib2

def ConvertTeam(team):
    return team

class EspnStatHeader(object):
    def __init__(self, soup):
        #for item in soup.find_all('td', {'class': 'playertableData'}):
        #    print(item)
        #for item in soup.find_all('td', {'class': 'playertableStat'}):
        #    print(item.a.string)
        #pass
        '''for now we are just going to hard code it. If we have time we will get this later'''
        self._data = [  'PASSING_C/A',
                        'PASSING_YDS',
                        'PASSING_TD',
                        'PASSING_INT',
                        'RUSHING_RUSH',
                        'RUSHING_YDS',
                        'RUSHING_TD',
                        'RECIEVING_REC',
                        'RECIEVING_YDS',
                        'RECIEVING_TD',
                        'OVERALL_PTS']

    def getHeaderInfo(self):
        return self._data


class EspnPlayer(object):
    def __init__(self, soup, header_info):
        self.stats = {}

        player_name_item = soup.find_all('td', {'class': 'playertablePlayerName'})[0]
        self.name = str(player_name_item.a.string)


        self.team = ConvertTeam(player_name_item.getText().encode('utf8').split(b', ')[1].split(b'\xc2\xa0')[0]).decode()
        self.pos = player_name_item.getText().encode('utf8').split(b'\xc2\xa0')[1].decode()

        player_stat_list = soup.find_all('td', {'class': 'playertableStat'})
        for count in range(len(player_stat_list)):
            if header_info.getHeaderInfo()[count] == 'PASSING_C/A':
                self.stats['COMPLETIONS'] = player_stat_list[count].string.split('/')[0]
                self.stats['ATTEMPTS'] = player_stat_list[count].string.split('/')[1]
            else:
                self.stats[header_info.getHeaderInfo()[count]] = player_stat_list[count].string

        for item in self.stats:
            if self.stats[item] == '--':
                self.stats[item] = float(0.0)
            else:
                self.stats[item] = float(self.stats[item])

class EspnParser(object):
    def __init__(self):
        self._players = []

    def AddPlayerStats(self, website):
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(website, None, headers)
        response = urllib2.urlopen(req)
        page = response.read() 

        soup = BeautifulSoup(page, 'html.parser')
        header = EspnStatHeader(soup.find_all('tr', {'class': 'playerTableBgRowSubhead tableSubHead'})[0])
        for item in soup.find_all('tr', {'class': 'pncPlayerRow'}):
            self._players.append(EspnPlayer(item, header))
            pass
    
    def getPlayers(self):
        return self._players

if __name__ == '__main__':
    import os

    path = 'file://%s' % (os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'EspnParserTest','TestData', 'QB1.html'))
    path2 = 'file://%s' % (os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'EspnParserTest','TestData', 'QB2.html'))
    print(path)
    TestClass = EspnParser()
    TestClass.AddPlayerStats(path)
    TestClass.AddPlayerStats(path2)
