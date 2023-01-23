# Create orders list
#menu = { 'Breakfast' : ['Spam n Eggs', 'Spam n Jam', 'Spam n Eggs'],
          # 'Lunch' : ['SLT (Spam-Lettuce-Tomato', 'PB&S (PB&Spam)'],
          # 'Dinner' : ['Spalad', 'Spamghetti', 'Spam Noodle Soup']}

menu = {'Knackered Spam': 0.5, 'Pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5, 'Cheeky Spam': 4.5}
orders = []


while(True):
    # See if the customer want to order antything else
    order = input('Can I take your order? (Q to Quit)')

    if order == 'Cheeky Spam':
        print('Sorry, we are all out of that!')
        continue
    elif (order.upper() == 'Q'):
        break
    # Find the order and add it to the list if it exists
    found = menu.get(order) # Try to get the menu item
    if found:
        orders.append(order) # If it exists, add it to the list
    else:
        print("Menu item doesn't exist")

    # See if the customer wants to order anything else
    order = input('Anything else? (Q to Quit)')
    # If we dont change "order" in the loop
print(orders)