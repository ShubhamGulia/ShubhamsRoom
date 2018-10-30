stocks={
    'GOOG': 434,
    'AAPL': 324,
    'FB': 44,
    'AMZN': 623,
    'F': 34,
    'MSFT': 439,
}

# (434, GOOG) (324, AAPL)

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)