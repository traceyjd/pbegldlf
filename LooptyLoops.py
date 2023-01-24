# For loop - For each item in our list do this
# Average price
total = 0
prices = [2.50, 3.50, 4.50]

for price in prices:
    print('Price is', price)
    total = total + price
    print('total is', total)

average = total/len(prices) # The length function gives us all the prices in the list
print('average is', average)

