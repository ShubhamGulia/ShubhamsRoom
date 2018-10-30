import heapq

grades= [10,20,30,80,40]

print(heapq.nlargest(3,grades))


stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 801},
    {'ticker': 'FB', 'price': 52},
    {'ticker': 'MSFT', 'price': 312},
    {'ticker': 'TUNA', 'price': 68}
]

print(heapq.nlargest(3, stocks, key=lambda stock: stock['price']))