
class FFTodayData(object):
    def __init__(self):

        import Parser

        self.quarter_backs = []
        self.runningbacks = []
        self.widerecievers = []
        self.tightends = []
        self.defense = []

        qb_parser = Parser.QBParser()
        qb_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=10&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=0')
        qb_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=10&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=1')
        self.quarter_backs = qb_parser.getPlayers()

        rb_parser = Parser.RBParser()
        rb_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=20&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=0')
        rb_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=20&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=1')
        rb_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=20&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=2')
        self.runningbacks = rb_parser.getPlayers()

        wr_parser = Parser.WRParser()
        wr_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=30&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=0')
        wr_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=30&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=1')
        wr_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=30&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=2')
        wr_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=30&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=3')
        self.widerecievers = wr_parser.getPlayers()

        te_parser = Parser.TEParser()
        te_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=40&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=0')
        te_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=40&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=1')
        self.tightends = te_parser.getPlayers()

        dl_parser = Parser.DLParser()
        dl_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=50&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=0')
        dl_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=50&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=1')
        dl_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=50&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=2')
        self.defense.append(dl_parser.getPlayers())

        lb_parser = Parser.LBParser()
        lb_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=60&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=0')
        lb_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=60&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=1')
        lb_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=60&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=2')
        self.defense.append(lb_parser.getPlayers())

        db_parser = Parser.DBParser()
        db_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=70&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=0')
        db_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=70&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=1')
        db_parser.AddPlayerStats('http://www.fftoday.com/rankings/playerproj.php?Season=2016&PosID=70&LeagueID=1&order_by=FFPts&sort_order=DESC&cur_page=2')
        self.defense.append(db_parser.getPlayers())


if __name__ == '__main__':
    data = FFTodayData()