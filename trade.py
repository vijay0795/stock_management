from datetime import datetime
from enum import Enum

class TradeIndicator(Enum):
    BUY='BUY'
    SELL = 'SELL'

class Trade:
    def __init__(self,quantity,timestamp,indicator,price):
        if quantity <=0 :
            raise ValueError('Quantity cannot be 0')
        if price <=0 :
            raise ValueError('Price cannot be 0')
        
        if not isinstance(indicator , TradeIndicator):
            raise ValueError("Indicator must be Buy or Sell")
        
        self.quantity=quantity
        self.timestamp = timestamp
        self.indicator = indicator
        self.price = price

    def __repr__(self):
        return(f"Trade(quantity={self.quantity}, "
            f"timestamp={self.timestamp}, "
            f"indicator={self.indicator.value}, "
            f"price={self.price})")


