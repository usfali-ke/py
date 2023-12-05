# First, loop over the items of the stocks dictionary
# Second, increase the price by 2% and add the item to the new dictionary (new_stocks).

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

new_stocks = {}
for symbol, price in stocks.items():
    new_stocks[symbol] = price*1.02

print(new_stocks)

# Below example shows how to use dictionary comprehension to achieve the same result:
new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}
print(new_stocks)

# First, iterate over the item of the stocks dictionary
# Then, add the item to the selected_stocks dictionary if the price is greater than 200
selected_stocks = {}
for symbol, price in stocks.items():
    if price > 200:
        selected_stocks[symbol] = price
print(selected_stocks)

# Using Python dictionary comprehension to filter a dictionary
selected_stocks = {symbol: price for (symbol, price) in stocks.items() if price > 200 }
print(selected_stocks)



