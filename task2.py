stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 280
}
portfolio = {}
total_value = 0
print("Welcome to the Stock Portfolio Tracker")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
print("Type 'done' to finish entering your stocks.")
while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Invalid stock symbol.")
        continue
    quantity = input("Enter quantity of shares: ")
    if not quantity.isdigit():
        print("Invalid quantity.")
        continue
    quantity = int(quantity)
    value = stock_prices[stock] * quantity
    total_value += value
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity
print("\nYour Stock Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    print(f"{stock}: {quantity} shares at ${price} each")
print("Total Investment Value: $", total_value)