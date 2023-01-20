# Create our Monty Python Restaurant Menu

# For each British slang word, lets create a menu item made with Spam

slang = ['Knackered', 'Pip pip', 'Squidgy', 'Smashing']


menu = []                      # For each word in our list, we'll concatenate Spam to it, and we'll add to our menu list
for word in slang:
    menu.append(word + ' Spam')

print(menu)

#  Assigning prices to our Menu Items
menu = ['Knackered Spam', 'Pip pip Spam', 'Squidgy Spam', 'Smashing Spam']
menu_prices = {}
price = 0.50
for item in menu:
    menu_prices[item] = price
    price = price + 1

print(menu_prices)