def maxProfit_bruteforce (prices):
   max_price = 0

   for i, price in enumerate(price):
       for j in range(i, len(price)):
           max_price = max(price[j] - price, max_price)

   return

