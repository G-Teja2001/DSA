prices = [7, 1, 5, 3, 6, 4]

days = len(prices)
buyingPrice = float('inf')
profit = 0
for i in range(days):
    todayPrice = prices[i]
    if i != 0:
        sellingPrice = todayPrice
        profit = max(sellingPrice - buyingPrice, profit)
    buyingPrice = min(buyingPrice, todayPrice)

print(profit)