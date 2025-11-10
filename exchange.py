import math
from stock import Stock , CommonStock , PreferredStock

class StockExchange:

    def __init__(self):
        self.stocks = {}

    def add_stock(self,stock):
        self.stocks[stock.stock_symbol] = stock

    def get_stock(self,stock_symbol):
        return self.stocks[stock_symbol]


    def calculate_gbce_all_share_index(self):
        prices = []
        for stock in self.stocks.values():
            try:
                vwsp = stock.calculate_volume_weighted_stock_price()
                prices.append(vwsp)
            except ValueError:
                continue

        log_sum = sum(math.log(price) for price in prices)
        geometric_mean = math.exp(log_sum / len(prices))


        return geometric_mean
