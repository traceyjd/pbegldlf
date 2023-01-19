

# Create orders list
#menu = { 'Breakfast' : ['Spam n Eggs', 'Spam n Jam', 'Spam n Eggs'],
          # 'Lunch' : ['SLT (Spam-Lettuce-Tomato', 'PB&S (PB&Spam)'],
          # 'Dinner' : ['Spalad', 'Spamghetti', 'Spam Noodle Soup']}

menu = {'Knackered Spam': 0.5, 'Pip pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5}
orders = []
order = input('What would you like to order? (Q to Quit)')

while (order.upper() != 'Q'):
    # Find the order and add it to the list if it exists

    found = menu.get(order) # Try to get the menu item
    if found:
        orders.append(order) # If it exists, add it to the list
    else:
        print("Menu item doesn't exist")

    # See if the customer wants to order anything else

    # If we dont change "order" in the loop

    # See if the customer wnat to order antything else
    order = input('Do you want to order antything else? (Q to Quit)')

print(orders)