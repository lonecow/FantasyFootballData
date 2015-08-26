'''
Created on Aug 23, 2015

@author: robertbitel
'''

import urllib2

def ConvertTeam(team):
    return team

class CurrentRosterStatHeader(object):
    def __init__(self, soup):
        #for item in soup.find_all('td', {'class': 'playertableData'}):
        #    print(item)
        #for item in soup.find_all('td', {'class': 'playertableStat'}):
        #    print(item.a.string)
        #pass
        '''for now we are just going to hard code it. If we have time we will get this later'''
        self._data = [  ('OWNER',           2)]

    def getHeaderInfo(self):
        return self._data


class CurrentRosterPlayer(object):
    def __init__(self, soup, header_info):
        self.stats = {}

        info_list = soup.split('~')
        self.name = info_list[0].split(', ')[0]
        self.team = info_list[0].split(', ')[1].split('\xa0')[0]
        self.pos = info_list[0].split(', ')[1].split('\xa0')[1]

        for (stat, line_num) in header_info.getHeaderInfo():
            self.stats[stat] = info_list[line_num]


class CurrentRosterParser(object):
    def __init__(self):
        self._players = []

    def AddPlayerStats(self, website):
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(website, None, headers)
        response = urllib2.urlopen(req)
        page = response.read() 

        header = CurrentRosterStatHeader('')
        for item in page.split('\n'):
            if '~' in item:
                self._players.append(CurrentRosterPlayer(item, header))
            pass
    
    def getPlayers(self):
        return self._players

if __name__ == '__main__':
    import os
    import urllib
    import urlparse

    def path2url(path):
        return urlparse.urljoin(
        'file:', urllib.pathname2url(path))


    path = path2url(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'PlayerData.txt'))
    TestClass = CurrentRosterParser()
    TestClass.AddPlayerStats(path)
