'''
Created on Aug 23, 2015

@author: robertbitel
'''

try:
    import urllib2  # @UnresolvedImport @UnusedImport
except:
    import urllib.request as urllib2  # @Reimport

from bs4 import BeautifulSoup

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

    def GetColumnName(self, index):
        name_ret = None
        for name, column_idx in self._data:
            if index == column_idx:
                name_ret = name
        return name_ret


class CurrentRosterPlayer(object):
    def __init__(self, soup, header_info):
        self.stats = {}

        table_columns = soup.find_all('td')


        self.name = str(table_columns[0].a.string)

        self.team = ConvertTeam(table_columns[0].getText().encode('utf8').split(b', ')[1].split(b'\xc2\xa0')[0]).decode()
        self.pos =table_columns[0].getText().encode('utf8').split(b'\xc2\xa0')[1].decode()

        self.owner = table_columns[2].string


    def __eq__(self, Right):
        if self is None and Right is None:
            return True
        elif Right is None:
            return False
        else:
            return (self.name == Right.name) and (self.pos == Right.pos) and (self.team == Right.team)


class CurrentRosterParser(object):
    def __init__(self):
        self._players = []

    def AddPlayerStats(self, website):
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(website, None, headers)
        response = urllib2.urlopen(req)
        page = response.read() 

        soup = BeautifulSoup(page, 'html.parser')
        header = CurrentRosterStatHeader(soup)
        for item in soup.find_all('tr', {'class': 'pncPlayerRow'}):
            self._players.append(CurrentRosterPlayer(item, header))
            pass

    def getPlayers(self):
        return self._players


if __name__ == '__main__':
    import os
    try:
        import urllib.request as urllib #@UnusedImport
    except:
        import urllib #@Reimport
    try:
        import urllib.parse as urlparse #@UnusedImport
    except:
        import urlparse #@UnresolvedImport @Reimport

    def path2url(path):
        return urlparse.urljoin(
        'file:', urllib.pathname2url(path))  # @UndefinedVariable


    path = 'file:///%s' % (os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'Players', 'Players1.html')))
    TestClass = CurrentRosterParser()
    TestClass.AddPlayerStats(path)
