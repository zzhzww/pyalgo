from pyalgotrade import strategy
from pyalgotrade.cn.csvfeed import Feed


class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        strategy.BacktestingStrategy.__init__(self, feed)
        self.__instrument = instrument

    def onBars(self, bars):
        bar = bars[self.__instrument]
        self.info(bar.getClose())


def testStrategy():


    from pyalgotrade import bar

    strat = MyStrategy
    instrument = '600288'
    market = 'SH'
    fromDate = '20150101'
    toDate = '20150601'
    frequency = bar.Frequency.MINUTE


    import os

    if frequency == bar.Frequency.MINUTE:
        path = os.path.join('..', 'histdata', 'minute')
    elif frequency == bar.Frequency.DAY:
        path = os.path.join('..', 'histdata', 'day')
    filepath = os.path.join(path, instrument + market + ".csv")

#############################################don't change ############################33
    from pyalgotrade.cn.csvfeed import Feed

    barfeed = Feed(frequency)
    barfeed.setDateTimeFormat('%Y-%m-%d %H:%M:%S')
    barfeed.loadBars(instrument, market, fromDate, toDate, filepath)

    pyalgotrade_id = instrument + '.' + market
    strat = strat(barfeed, pyalgotrade_id)
    print filepath
    # strat.run()
if __name__ == "__main__":
    testStrategy()
