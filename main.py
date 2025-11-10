from stock import CommonStock, PreferredStock
from trade import TradeIndicator
from exchange import StockExchange


def main():
    exchange = StockExchange()
    
    tea = CommonStock("TEA", 0, 100)
    pop = CommonStock("POP", 8, 100)
    ale = CommonStock("ALE", 23, 60)
    gin = PreferredStock("GIN", 8, 100, 0.02)
    joe = CommonStock("JOE", 13, 250)
    
    exchange.add_stock(tea)
    exchange.add_stock(pop)
    exchange.add_stock(ale)
    exchange.add_stock(gin)
    exchange.add_stock(joe)
    
    print("Sample Stock Calculations")
    print("-" * 40)
    
    price = 100
    print(f"\nPOP at price {price}:")
    print(f"Dividend Yield: {pop.calculate_dividend_yield(price):.4f}")
    print(f"P/E Ratio: {pop.calculate_pe_ratio(price):.2f}")
    
    print(f"\nGIN at price {price}:")
    print(f"Dividend Yield: {gin.calculate_dividend_yield(price):.4f}")
    print(f"P/E Ratio: {gin.calculate_pe_ratio(price):.2f}")
    
    print("\n\nRecording Trades")
    print("-" * 40)
    
    pop.record_trade(100, TradeIndicator.BUY, 150)
    pop.record_trade(50, TradeIndicator.SELL, 155)
    pop.record_trade(75, TradeIndicator.BUY, 152)
    
    ale.record_trade(200, TradeIndicator.BUY, 180)
    ale.record_trade(100, TradeIndicator.SELL, 185)
    
    gin.record_trade(150, TradeIndicator.BUY, 110)
    gin.record_trade(80, TradeIndicator.SELL, 115)
    
    joe.record_trade(120, TradeIndicator.BUY, 200)
    joe.record_trade(90, TradeIndicator.SELL, 205)
    
    tea.record_trade(80, TradeIndicator.BUY, 120)
    
    print(f"Trades recorded for POP: {len(pop.trades)}")
    print(f"Trades recorded for ALE: {len(ale.trades)}")
    print(f"Trades recorded for GIN: {len(gin.trades)}")
    print(f"Trades recorded for JOE: {len(joe.trades)}")
    print(f"Trades recorded for TEA: {len(tea.trades)}")
    
    print("\n\nVolume Weighted Stock Prices")
    print("-" * 40)
    
    print(f"POP: {pop.calculate_volume_weighted_stock_price():.2f}")
    print(f"ALE: {ale.calculate_volume_weighted_stock_price():.2f}")
    print(f"GIN: {gin.calculate_volume_weighted_stock_price():.2f}")
    print(f"JOE: {joe.calculate_volume_weighted_stock_price():.2f}")
    print(f"TEA: {tea.calculate_volume_weighted_stock_price():.2f}")
    
    print("\n\nGBCE All Share Index")
    print("-" * 40)
    
    index = exchange.calculate_gbce_all_share_index()
    print(f"Index: {index:.2f}")


if __name__ == "__main__":
    main()
