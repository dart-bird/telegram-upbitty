import pyupbit
import stockstats
import time
import json
from .path_helper import PathHelper

class UpbitUtil():
    def __init__(self):
        super().__init__()
        self.tickers = pyupbit.get_tickers(fiat='KRW') 
    def get_ticker_price(self, ticker):
        return pyupbit.get_current_price(ticker=ticker)
    def reload_tickers(self):
        self.tickers = pyupbit.get_tickers(fiat='KRW')
    def get_tickers(self):
        return pyupbit.get_tickers(fiat='KRW')
    def get_rsi(self, ticker : str, interval : str):
        coin_data = pyupbit.get_ohlcv(ticker=ticker, interval=interval, count=500)
        stock = stockstats.StockDataFrame.retype(coin_data)
        return stock['rsi_14'][-1]
    def get_can_buy(self, ticker : str, interval : str):
        rsi = self.get_rsi(ticker, interval)
        if float(rsi) < 25:
            return True
        return False
    def get_target_tickers(self, tickers : str, interval : str, default = True):
        target_tickers = []
        for ticker in tickers:
            if self.get_can_buy(ticker=ticker, interval=interval) == True:
                target_tickers.append(ticker)
            if default != True: time.sleep(0.04)
        return target_tickers

    def get_favorite(self):
        f = open(PathHelper.get_user_data_path())
        user_data = json.load(f)
        favorite = user_data['favorite']
        return favorite