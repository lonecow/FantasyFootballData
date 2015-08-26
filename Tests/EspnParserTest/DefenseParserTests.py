'''
Created on Aug 23, 2015

@author: robertbitel
'''
import unittest
import os

import urllib
import urlparse

from EspnParser import DefenseParser

def path2url(path):
    return urlparse.urljoin(
      'file:', urllib.pathname2url(path))

path = path2url(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'DEF1.html'))

class TestGetsCorrectNumberOfPlayers(unittest.TestCase):
    def setUp(self):
        self.TestClass = DefenseParser()
        self.TestClass.AddPlayerStats(path)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(len(players), 482)
        pass


class TestGetCorrectFirstPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = DefenseParser()
        self.TestClass.AddPlayerStats(path)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[0].name, 'Lavonte David')
        self.assertEqual(players[0].team, 'TB')
        self.assertEqual(players[0].pos, 'LB')
        self.assertEqual(players[0].stats['TACKLES'], 118.0)
        self.assertEqual(players[0].stats['ASSIST'], 47.4)
        self.assertEqual(players[0].stats['SACKS'], 2.9)
        self.assertEqual(players[0].stats['PASSESDEFENSED'], 6.3)
        self.assertEqual(players[0].stats['INTERCEPTIONS'], 1.5)
        self.assertEqual(players[0].stats['FUMBLESRECOVERED'], 3.3)
        self.assertEqual(players[0].stats['FUMBLESFORCED'], 1.0)
        self.assertEqual(players[0].stats['DEFENSEIVETDS'], 0.0)


class TestGetCorrectSecondPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = DefenseParser()
        self.TestClass.AddPlayerStats(path)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[1].name, 'Harrison Smith')
        self.assertEqual(players[1].team, 'Min')
        self.assertEqual(players[1].pos, 'DB')
        self.assertEqual(players[1].stats['TACKLES'], 102.0)
        self.assertEqual(players[1].stats['ASSIST'], 28.3)
        self.assertEqual(players[1].stats['SACKS'], 2.7)
        self.assertEqual(players[1].stats['PASSESDEFENSED'], 10.5)
        self.assertEqual(players[1].stats['INTERCEPTIONS'], 4.8)
        self.assertEqual(players[1].stats['FUMBLESRECOVERED'], 0.9)
        self.assertEqual(players[1].stats['FUMBLESFORCED'], 0.0)
        self.assertEqual(players[1].stats['DEFENSEIVETDS'], 0.02)

class TestGetCorrectSixteenthPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = DefenseParser()
        self.TestClass.AddPlayerStats(path)



    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[15].name, 'Morgan Burnett')
        self.assertEqual(players[15].team, 'GB')
        self.assertEqual(players[15].pos, 'DB')
        self.assertEqual(players[15].stats['TACKLES'], 87.0)
        self.assertEqual(players[15].stats['ASSIST'], 38.0)
        self.assertEqual(players[15].stats['SACKS'], 1.8)
        self.assertEqual(players[15].stats['PASSESDEFENSED'], 5.6)
        self.assertEqual(players[15].stats['INTERCEPTIONS'], 1.1)
        self.assertEqual(players[15].stats['FUMBLESRECOVERED'], 0.5)
        self.assertEqual(players[15].stats['FUMBLESFORCED'], 0.5)
        self.assertEqual(players[15].stats['DEFENSEIVETDS'], 0.02)


class TestGetCorrectOneHundredSixtythPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = DefenseParser()
        self.TestClass.AddPlayerStats(path)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[159].name, 'Robert Quinn')
        self.assertEqual(players[159].team, 'StL')
        self.assertEqual(players[159].pos, 'DL')
        self.assertEqual(players[159].stats['TACKLES'], 43.5)
        self.assertEqual(players[159].stats['ASSIST'], 7.2)
        self.assertEqual(players[159].stats['SACKS'], 14.0)
        self.assertEqual(players[159].stats['PASSESDEFENSED'], 4.4)
        self.assertEqual(players[159].stats['INTERCEPTIONS'], 0.0)
        self.assertEqual(players[159].stats['FUMBLESRECOVERED'], 5.7)
        self.assertEqual(players[159].stats['FUMBLESFORCED'], 0.9)
        self.assertEqual(players[159].stats['DEFENSEIVETDS'], 0.2)

class TestGetCorrectFourHundredEightySecondPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = DefenseParser()
        self.TestClass.AddPlayerStats(path)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[481].name, 'Paul Dawson')
        self.assertEqual(players[481].team, 'Cin')
        self.assertEqual(players[481].pos, 'LB')
        self.assertEqual(players[481].stats['TACKLES'], 0.04)
        self.assertEqual(players[481].stats['ASSIST'], 0.07)
        self.assertEqual(players[481].stats['SACKS'], 0.0)
        self.assertEqual(players[481].stats['PASSESDEFENSED'], 0.0)
        self.assertEqual(players[481].stats['INTERCEPTIONS'], 0.0)
        self.assertEqual(players[481].stats['FUMBLESRECOVERED'], 0.0)
        self.assertEqual(players[481].stats['FUMBLESFORCED'], 0.0)
        self.assertEqual(players[481].stats['DEFENSEIVETDS'], 0.0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()