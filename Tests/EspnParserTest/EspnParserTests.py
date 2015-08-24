'''
Created on Aug 23, 2015

@author: robertbitel
'''
import unittest
import os

from EspnParser import EspnParser


path = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'QB1.html'))
path2 = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'QB2.html'))

class TestGetsCorrectNumberOfPlayers(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnParser()
        self.TestClass.AddPlayerStats(path)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(len(players), 40)
        pass

class TestGetsCorrectNumberOfPlayersTwoDownloads(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnParser()
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(len(players), 80)
        pass


class TestGetCorrectFirstPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnParser()
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[0].name, 'Aaron Rodgers')
        self.assertEqual(players[0].team, 'GB')
        self.assertEqual(players[0].pos, 'QB')
        self.assertEqual(players[0].stats['COMPLETIONS'], 347)
        self.assertEqual(players[0].stats['ATTEMPTS'], 538)
        self.assertEqual(players[0].stats['PASSING_YDS'], 4317)
        self.assertEqual(players[0].stats['PASSING_TD'], 35)
        self.assertEqual(players[0].stats['PASSING_INT'], 8)
        self.assertEqual(players[0].stats['RUSHING_RUSH'], 50)
        self.assertEqual(players[0].stats['RUSHING_YDS'], 256)
        self.assertEqual(players[0].stats['RUSHING_TD'], 2)
        self.assertEqual(players[0].stats['RECIEVING_REC'], 0)
        self.assertEqual(players[0].stats['RECIEVING_YDS'], 0)
        self.assertEqual(players[0].stats['RECIEVING_TD'], 0)


class TestGetCorrectSecondPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnParser()
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[1].name, 'Andrew Luck')
        self.assertEqual(players[1].team, 'Ind')
        self.assertEqual(players[1].pos, 'QB')
        self.assertEqual(players[1].stats['COMPLETIONS'], 383)
        self.assertEqual(players[1].stats['ATTEMPTS'], 621)
        self.assertEqual(players[1].stats['PASSING_YDS'], 4484)
        self.assertEqual(players[1].stats['PASSING_TD'], 36)
        self.assertEqual(players[1].stats['PASSING_INT'], 16)
        self.assertEqual(players[1].stats['RUSHING_RUSH'], 57)
        self.assertEqual(players[1].stats['RUSHING_YDS'], 268)
        self.assertEqual(players[1].stats['RUSHING_TD'], 2)
        self.assertEqual(players[1].stats['RECIEVING_REC'], 0)
        self.assertEqual(players[1].stats['RECIEVING_YDS'], 0)
        self.assertEqual(players[1].stats['RECIEVING_TD'], 0)


class TestGetCorrectFourtythPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnParser()
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)



    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[39].name, 'EJ Manuel')
        self.assertEqual(players[39].team, 'Buf')
        self.assertEqual(players[39].pos, 'QB')
        self.assertEqual(players[39].stats['COMPLETIONS'], 16)
        self.assertEqual(players[39].stats['ATTEMPTS'], 28)
        self.assertEqual(players[39].stats['PASSING_YDS'], 184)
        self.assertEqual(players[39].stats['PASSING_TD'], 1)
        self.assertEqual(players[39].stats['PASSING_INT'], 1)
        self.assertEqual(players[39].stats['RUSHING_RUSH'], 4)
        self.assertEqual(players[39].stats['RUSHING_YDS'], 11)
        self.assertEqual(players[39].stats['RUSHING_TD'], 0)
        self.assertEqual(players[39].stats['RECIEVING_REC'], 0)
        self.assertEqual(players[39].stats['RECIEVING_YDS'], 0)
        self.assertEqual(players[39].stats['RECIEVING_TD'], 0)

class TestGetCorrectFortyFirstPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnParser()
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[40].name, 'Brandon Weeden')
        self.assertEqual(players[40].team, 'Dal')
        self.assertEqual(players[40].pos, 'QB')
        self.assertEqual(players[40].stats['COMPLETIONS'], 9)
        self.assertEqual(players[40].stats['ATTEMPTS'], 15)
        self.assertEqual(players[40].stats['PASSING_YDS'], 118)
        self.assertEqual(players[40].stats['PASSING_TD'], 1)
        self.assertEqual(players[40].stats['PASSING_INT'], 0)
        self.assertEqual(players[40].stats['RUSHING_RUSH'], 0)
        self.assertEqual(players[40].stats['RUSHING_YDS'], 1)
        self.assertEqual(players[40].stats['RUSHING_TD'], 0)
        self.assertEqual(players[40].stats['RECIEVING_REC'], 0)
        self.assertEqual(players[40].stats['RECIEVING_YDS'], 0)
        self.assertEqual(players[40].stats['RECIEVING_TD'], 0)

class TestGetCorrectEightythPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnParser()
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[79].name, 'Chris Redman')
        self.assertEqual(players[79].team, 'FA')
        self.assertEqual(players[79].pos, 'QB')
        self.assertEqual(players[79].stats['COMPLETIONS'], 0)
        self.assertEqual(players[79].stats['ATTEMPTS'], 0)
        self.assertEqual(players[79].stats['PASSING_YDS'], 0)
        self.assertEqual(players[79].stats['PASSING_TD'], 0)
        self.assertEqual(players[79].stats['PASSING_INT'], 0)
        self.assertEqual(players[79].stats['RUSHING_RUSH'], 0)
        self.assertEqual(players[79].stats['RUSHING_YDS'], 0)
        self.assertEqual(players[79].stats['RUSHING_TD'], 0)
        self.assertEqual(players[79].stats['RECIEVING_REC'], 0)
        self.assertEqual(players[79].stats['RECIEVING_YDS'], 0)
        self.assertEqual(players[79].stats['RECIEVING_TD'], 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()