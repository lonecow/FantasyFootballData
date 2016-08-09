'''
Created on Aug 23, 2015

@author: robertbitel
'''

from bs4 import BeautifulSoup
try:
    import urllib2  # @UnresolvedImport @UnusedImport
except:
    import urllib.request as urllib2  # @Reimport

def removeJavaScript(content):
    contents = ''
    count = 0
    for line in content.split(b'\n'):
        copy_end_pos = len(line)

        if count != 0:
            copy_beg_pos = len(line)
        else:
            copy_beg_pos = 0

        if b'<script' in line:
            copy_end_pos = line.find(b'<script')
            count += line.count(b'<script')

        if b'</script' in line:
            count -= line.count(b'</script')
            if count == 0:
                copy_beg_pos = line.rfind(b'</script>') + len(b'</script>')

        contents += str(line[copy_beg_pos:copy_end_pos])
    return contents    


def ConvertTeam(team):
    team_list = {
                        'ARZ':'Ari',
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
                        'GBP':'GB',
                        'HOU':'Hou',
                        'IND':'Ind',
                        'JAC':'Jac',
                        'KCC':'KC',
                        'MIA':'Mia',
                        'MIN':'Min',
                        'NEP':'NE',
                        'NOR':'NO',
                        'NYG':'NYG',
                        'NYJ':'NYJ',
                        'OAK':'Oak',
                        'PHI':'Phi',
                        'PIT':'Pit',
                        'SDC':'SD',
                        'SEA':'Sea',
                        'SFO':'SF',
                        'STL':'StL',
                        'TBB':'TB',
                        'TEN':'Ten',
                        'WAS':'Wsh'}
    try:
        return team_list[team]
    except:
        return team

class DefenseStatHeader(object):
    def __init__(self, soup):
        #for item in soup.find_all('td', {'class': 'playertableData'}):
        #    print(item)
        #for item in soup.find_all('td', {'class': 'playertableStat'}):
        #    print(item.a.string)
        #pass
        '''for now we are just going to hard code it. If we have time we will get this later'''
        self._data = [  ('TACKLES',         4),
                        ('ASSIST',          5),
                        ('SACKS',           6),
                        ('PASSESDEFENSED',  7),
                        ('INTERCEPTIONS',   8),
                        ('FUMBLESRECOVERED',9),
                        ('FUMBLESFORCED',   10),
                        ('DEFENSEIVETDS',   11)]

    def getHeaderInfo(self):
        return self._data


class DefensePlayer(object):
    def __init__(self, soup, header_info):
        self.stats = {}

        player_stat_list = soup.find_all('td')

        self.name = player_stat_list[1].a.string
        self.name = '%s %s' % (self.name.split(', ')[1], self.name.split(', ')[0])
        self.team = ConvertTeam(player_stat_list[2].string)
        self.pos = player_stat_list[3].string

        for (stat, line_num) in header_info.getHeaderInfo():
            self.stats[stat] = float(player_stat_list[line_num].string)


class DefenseParser(object):
    def __init__(self):
        self._players = []

    def AddPlayerStats(self, website):
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(website, None, headers)
        response = urllib2.urlopen(req)
        page = removeJavaScript(response.read()) 
        open('test', 'w').write(page)

        soup = BeautifulSoup(page, 'html.parser')

        div_table = soup.find('div', {'class':'toolDiv'})
        table_info = div_table.table.find_all('tr')
        for item in table_info:
            if item.find_all('td', {'class':'playerLink'}):
                self._players.append(DefensePlayer(item, DefenseStatHeader(soup)))
            
        #header = DefenseStatHeader(soup.find_all('tr', {'class': 'playerTableBgRowSubhead tableSubHead'})[0])
        #for item in soup.find_all('tr', {'class': 'pncPlayerRow'}):
        #    self._players.append(DefensePlayer(item, header))
        #    pass
    
    def getPlayers(self):
        return self._players
        

if __name__ == '__main__':
    test = DefenseParser()
    test.AddPlayerStats('http://www.fantasysharks.com/apps/bert/forecasts/projections.php?League=&Position=98&scoring=1&Segment=522&uid=4')