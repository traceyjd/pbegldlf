
menu = {'Knackered Spam': 0.5, 'Pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5, 'Cheeky Spam': 4.5}
orders = []
order = input('What would you like to order? (Q to Quit)')

while (True):
    if order == 'Cheeky Spam':
        print('Sorry, we are all out of that!')
        continue

    if order.upper() == 'Q':
        break
    # Find the order and add it to the list if it exists

    found = menu.get(order) # Try to get the menu item
    if found:
        orders.append(order) # If it exists, add it to the list
    else:
        print("Menu item doesn't exist")

    # See if the customer wants to order anything else

    # If we dont change "order" in the loop

    # See if the customer want to order antything else
    order = input('Anything else? (Q to Quit)')

print(orders)