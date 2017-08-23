'''
Created on Aug 23, 2015

@author: robertbitel
'''

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
            return (self.name == Right.name) and (self.team == Right.team)

    def __str__(self):
        return ('Name: %s Team: %s Pos: %s Owner: %s' % (self.name, self.team, self.pos, self.owner))

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By

class EspnProtectedWebsiteGrabber():
    def __init__(self):
        self.driver = None

    def Connect(self):

        self.Disconnect()

        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : 'C:\\Users\\robert.bitel\\Downloads'}
        chromeOptions.add_experimental_option("prefs",prefs)
        chromedriver = '.\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

        self.driver.get('http://games.espn.com/ffl/freeagency?leagueId=182037&teamId=2')

        WebDriverWait(self.driver,1000).until(EC.presence_of_all_elements_located((By.XPATH,"(//iframe)")))
        frms = self.driver.find_elements_by_xpath("(//iframe)")

        for frame in frms:
            print(frame.id)
            print(frame.get_attribute("name"))
            if frame.get_attribute('name') == 'disneyid-iframe':
                break
        '''TODO they tend to change the frame this needs to be fixed '''
        self.driver.switch_to_frame(frame)

        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*/div/div/section/section/form/section/div[2]/div/label/span[2]/input')))
        password = self.driver.find_elements_by_xpath("//*/div/div/section/section/form/section/div[2]/div/label/span[2]/input")
        if len(password) > 0:
            password = password[0]

            username = self.driver.find_elements_by_xpath("//*/input[@type='email']")
            username = username[0]
            username.send_keys('lonecow@gmail.com')
            password.send_keys('WxFUua!e69')

            enter = self.driver.find_elements_by_xpath("//*[@id=\"did-ui\"]/div/div/section/section/form/section/div[3]/button[2]")
            enterBtn = enter[0]
            enterBtn.click()

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "playerTableContainerDiv")))

    def Disconnect(self):
        if self.driver != None:
            self.driver.quit()
            self.driver = None

    def GetWebsite(self, website):
        if self.driver != None:
            self.driver.get(website)
            return self.driver.page_source
        else:
            return ''

class CurrentRosterParser(object):
    def __init__(self):
        self._players = []
        self.driver = EspnProtectedWebsiteGrabber()
        self.driver.Connect()

    def AddPlayerStats(self, website):
        page = self.driver.GetWebsite(website)

        soup = BeautifulSoup(page, 'html.parser')
        header = CurrentRosterStatHeader(soup)
        for item in soup.find_all('tr', {'class': 'pncPlayerRow'}):
            self._players.append(CurrentRosterPlayer(item, header))
            pass

    def getPlayers(self):
        return self._players


if __name__ == '__main__':
    TestClass = CurrentRosterParser()
    TestClass.AddPlayerStats('http://games.espn.com/ffl/freeagency?leagueId=182037&teamId=2&seasonId=2017&seasonId=2016&=undefined&avail=4&context=freeagency&view=overview')
