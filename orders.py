

# Create orders list
menu = ['Knackered Spam', 'Pip pip Spam', 'Squidgy Spam', 'Smashing Spam']
orders []
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

    # See