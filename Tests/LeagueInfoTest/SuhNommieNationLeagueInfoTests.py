'''
Created on Aug 23, 2015

@author: robertbitel
'''
import unittest

from LeagueInfo import SuhNommieNationLeagueInfo

class TestPlayer(object):


    def __init__(self):
        self.stats = {}


class TestGetStartingPositions(unittest.TestCase):


    def setUp(self):
        self.TestClass = SuhNommieNationLeagueInfo()
        pass


    def runTest(self):
        testInfo = self.TestClass.GetPositionStartingCounts()
        self.assertEqual(testInfo['QB'], 2)
        self.assertEqual(testInfo['RB'], 2)
        self.assertEqual(testInfo['WR'], 3)
        self.assertEqual(testInfo['TE'], 1)
        self.assertEqual(testInfo['K'], 1)
        self.assertEqual(testInfo['D'], 3)


class TestGetMaxPositions(unittest.TestCase):


    def setUp(self):
        self.TestClass = SuhNommieNationLeagueInfo()
        pass


    def runTest(self):
        testInfo = self.TestClass.GetPositionMaxCounts()
        self.assertEqual(testInfo['QB'], 4)
        self.assertEqual(testInfo['RB'], 5)
        self.assertEqual(testInfo['WR'], 6)
        self.assertEqual(testInfo['TE'], 3)
        self.assertEqual(testInfo['K'], 2)
        self.assertEqual(testInfo['D'], 5)


class TestCalculatePoints1(unittest.TestCase):


    def setUp(self):
        self.TestClass = SuhNommieNationLeagueInfo()


        points_ary = [
                    ('COMPLETIONS',      1),
                    ('ATTEMPTS',         2),
                    ('PASSING_YDS',      3),
                    ('PASSING_TD',       4),
                    ('PASSING_INT',      5),
                    ('RUSHING_RUSH',     6),
                    ('RUSHING_YDS',      7),
                    ('RUSHING_TD',       8),
                    ('RECIEVING_REC',    9),
                    ('RECIEVING_YDS',    10),
                    ('RECIEVING_TD',     11),
                    ('SCORED_1-39,',     12),
                    ('ATTEMPTED_1-39,',  13),
                    ('SCORED_40-49,',    14),
                    ('ATTEMPTED_40-49,', 15),
                    ('SCORED_50+',       16),
                    ('ATTEMPTED_50+',    17),
                    ('SCORED_TOT',       18),
                    ('ATTEMPTED_TOT',    19),
                    ('SCORED_XP',        20),
                    ('ATTEMPTED_XP',     21)]

        self.TestPlayer = TestPlayer()

        for (stat, count) in points_ary:
            self.TestPlayer.stats[stat] = count
        pass


    def runTest(self):
        testInfo = self.TestClass.calculatePoints(self.TestPlayer)
        self.assertEqual(testInfo, 507.72)



class TestCalculateDefenseivePoints(unittest.TestCase):


    def setUp(self):
        self.TestClass = SuhNommieNationLeagueInfo()


        points_ary = [
                    ('TACKLES',         1),
                    ('ASSIST',          2),
                    ('SACKS',           3),
                    ('PASSESDEFENSED',  4),
                    ('INTERCEPTIONS',   5),
                    ('FUMBLESRECOVERED', 6),
                    ('FUMBLESFORCED',   7),
                    ('DEFENSEIVETDS',   8)]

        self.TestPlayer = TestPlayer()

        for (stat, count) in points_ary:
            self.TestPlayer.stats[stat] = count
        pass


    def runTest(self):
        testInfo = self.TestClass.calculatePoints(self.TestPlayer)
        self.assertEqual(testInfo, 195.2)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()