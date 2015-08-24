'''
Created on Aug 23, 2015

@author: robertbitel
'''
import unittest
import os

from EspnParser import EspnKickerParser


class TestGetsCorrectNumberOfPlayers(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnKickerParser()
        path = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker1.html'))
        self.TestClass.AddPlayerStats(path)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(len(players), 15)
        pass

class TestGetsCorrectNumberOfPlayersTwoDownloads(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnKickerParser()
        path = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker1.html'))
        path2 = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker2.html'))
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(len(players), 30)
        pass


class TestGetCorrectFirstPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnKickerParser()
        path = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker1.html'))
        path2 = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker2.html'))
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[0].name, 'Stephen Gostkowski')
        self.assertEqual(players[0].team, 'NE')
        self.assertEqual(players[0].stats['SCORED_1-39'], 16)
        self.assertEqual(players[0].stats['ATTEMPTED_1-39'], 17)
        self.assertEqual(players[0].stats['SCORED_40-49'], 8)
        self.assertEqual(players[0].stats['ATTEMPTED_40-49'], 10)
        self.assertEqual(players[0].stats['SCORED_50+'], 2)
        self.assertEqual(players[0].stats['ATTEMPTED_50+'], 3)
        self.assertEqual(players[0].stats['SCORED_TOT'], 26)
        self.assertEqual(players[0].stats['ATTEMPTED_TOT'], 30)
        self.assertEqual(players[0].stats['SCORED_XP'], 52)
        self.assertEqual(players[0].stats['ATTEMPTED_XP'], 52)


class TestGetCorrectSecondPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnKickerParser()
        path = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker1.html'))
        path2 = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker2.html'))
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[1].name, 'Adam Vinatieri')
        self.assertEqual(players[1].team, 'Ind')
        self.assertEqual(players[1].stats['SCORED_1-39'], 14)
        self.assertEqual(players[1].stats['ATTEMPTED_1-39'], 15)
        self.assertEqual(players[1].stats['SCORED_40-49'], 8)
        self.assertEqual(players[1].stats['ATTEMPTED_40-49'], 9)
        self.assertEqual(players[1].stats['SCORED_50+'], 3)
        self.assertEqual(players[1].stats['ATTEMPTED_50+'], 4)
        self.assertEqual(players[1].stats['SCORED_TOT'], 25)
        self.assertEqual(players[1].stats['ATTEMPTED_TOT'], 28)
        self.assertEqual(players[1].stats['SCORED_XP'], 50)
        self.assertEqual(players[1].stats['ATTEMPTED_XP'], 50)


class TestGetCorrectFifteenthPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnKickerParser()
        path = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker1.html'))
        path2 = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker2.html'))
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)



    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[14].name, 'Nick Novak')
        self.assertEqual(players[14].team, 'SD')
        self.assertEqual(players[14].stats['SCORED_1-39'], 18)
        self.assertEqual(players[14].stats['ATTEMPTED_1-39'], 19)
        self.assertEqual(players[14].stats['SCORED_40-49'], 6)
        self.assertEqual(players[14].stats['ATTEMPTED_40-49'], 7)
        self.assertEqual(players[14].stats['SCORED_50+'], 3)
        self.assertEqual(players[14].stats['ATTEMPTED_50+'], 4)
        self.assertEqual(players[14].stats['SCORED_TOT'], 27)
        self.assertEqual(players[14].stats['ATTEMPTED_TOT'], 30)
        self.assertEqual(players[14].stats['SCORED_XP'], 38)
        self.assertEqual(players[14].stats['ATTEMPTED_XP'], 38)


class TestGetCorrectSixteenthPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnKickerParser()
        path = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker1.html'))
        path2 = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker2.html'))
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[15].name, 'Chandler Catanzaro')
        self.assertEqual(players[15].team, 'Ari')
        self.assertEqual(players[15].stats['SCORED_1-39'], 16)
        self.assertEqual(players[15].stats['ATTEMPTED_1-39'], 17)
        self.assertEqual(players[15].stats['SCORED_40-49'], 9)
        self.assertEqual(players[15].stats['ATTEMPTED_40-49'], 10)
        self.assertEqual(players[15].stats['SCORED_50+'], 2)
        self.assertEqual(players[15].stats['ATTEMPTED_50+'], 3)
        self.assertEqual(players[15].stats['SCORED_TOT'], 27)
        self.assertEqual(players[15].stats['ATTEMPTED_TOT'], 30)
        self.assertEqual(players[15].stats['SCORED_XP'], 36)
        self.assertEqual(players[15].stats['ATTEMPTED_XP'], 36)

class TestGetCorrectThirtythPlayer(unittest.TestCase):
    def setUp(self):
        self.TestClass = EspnKickerParser()
        path = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker1.html'))
        path2 = 'file://%s' % (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TestData', 'Kicker2.html'))
        self.TestClass.AddPlayerStats(path)
        self.TestClass.AddPlayerStats(path2)


    def tearDown(self):
        pass


    def runTest(self):
        players = self.TestClass.getPlayers()
        self.assertEqual(players[29].name, 'Josh Scobee')
        self.assertEqual(players[29].team, 'Jac')
        self.assertEqual(players[29].stats['SCORED_1-39'], 14)
        self.assertEqual(players[29].stats['ATTEMPTED_1-39'], 15)
        self.assertEqual(players[29].stats['SCORED_40-49'], 9)
        self.assertEqual(players[29].stats['ATTEMPTED_40-49'], 11)
        self.assertEqual(players[29].stats['SCORED_50+'], 3)
        self.assertEqual(players[29].stats['ATTEMPTED_50+'], 5)
        self.assertEqual(players[29].stats['SCORED_TOT'], 26)
        self.assertEqual(players[29].stats['ATTEMPTED_TOT'], 31)
        self.assertEqual(players[29].stats['SCORED_XP'], 28)
        self.assertEqual(players[29].stats['ATTEMPTED_XP'], 28)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()