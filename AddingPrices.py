
#  Assigning prices to our Menu Items
menu = ['Knackered Spam', 'Pip pip Spam', 'Squidgy Spam', 'Smashing Spam']
menu_prices = {}
price = 0.50
for item in menu:
    menu_prices[item] = price
    price = price + 1

print(menu_prices)

for name, price in menu_prices.items():
    print(name, ': £', format(price, '.2f'), sep='') # f for float and .2 for decimals places


# Note: To get a list of the keys in a dictionary, use dict_menu.keys()
#       and to get a list of the values in a dictionry, use dict_name.values()

#  For loops allow you to loop a certain number of times
#  While loops allow you to loop until a condition is True or something happens

