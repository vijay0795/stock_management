from trade import Trade
from datetime import datetime,timedelta

class Stock:
    def __init__(self,stock_symbol, last_dividend,par_value):
        
        self.stock_symbol = stock_symbol
        self.last_dividend = last_dividend
        self.par_value = par_value
        self.trades=[]

    def calculate_dividend_yield(self,price):
        if price <= 0:
            raise ValueError('Price cannot be 0 or negative')
        return self.last_dividend/price

    def calculate_pe_ratio(self,price):
        if self.last_dividend == 0:
            raise ValueError('Dividend cannot be 0')
        return price/self.last_dividend
    
    def record_trade(self,quantity,indicator,price):
        trade = Trade(quantity,datetime.now(),indicator,price)
        self.trades.append(trade)

        return trade

    def calculate_volume_weighted_stock_price(self,delta_in_minutes=5):
        current_time = datetime.now()
        delta_time = current_time - timedelta(minutes=delta_in_minutes)
        latest_trades = [t for t in self.trades if t.timestamp >= delta_time]

        sum_of_price_per_quantity = sum(trade.price * trade.quantity for trade in latest_trades)
        sum_of_quantity = sum(trade.quantity for trade in latest_trades)


        return sum_of_price_per_quantity / sum_of_quantity

class CommonStock(Stock):
    
    def __init__(self,stock_symbol, last_dividend,par_value):
        super().__init__(stock_symbol, last_dividend,par_value)
    
   

class PreferredStock(Stock):
    def __init__(self,stock_symbol, last_dividend,par_value,fixed_dividend):
        super().__init__(stock_symbol, last_dividend,par_value)
        self.fixed_dividend=fixed_dividend
        
    def calculate_pe_ratio(self,price):
        last_dividend = self.fixed_dividend * self.par_value
        if last_dividend == 0:
            raise ValueError('Dividend cannot be 0')
        return price/last_dividend


    def calculate_dividend_yield(self,price):
        return (self.fixed_dividend * self.par_value) / price
    
  
