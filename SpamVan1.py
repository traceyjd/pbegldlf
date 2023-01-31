#  Print the menu

#  Take an order

#  Calculate the total bill

def print_menu(menu):
    for name, price in menu.items():
        print(name, ': $', format(price, '.2f'), sep='')  # indented : contents of the function are indented
    # We dont need to return anything as we are just printing

def get_order(menu):
    orders = []
    order = input('What would you like to order? (Q to Quit)')

    while (order.upper() != 'Q'):
        # Find the order and add it to the list if it exists
        found = menu.get(order)  # Try to get the menu item
        if found:
            orders.append(order)  # If it exists, add it to the list
        else:
            print("Menu item doesn't exist")

        # See if the customer wants to order anything else
        # If we dont change "order" in the loop
        # See if the customer want to order antything else
        order = input('Anything else? (Q to Quit)')
    return orders

def main():
    menu = {'Knackered Spam': 0.5, 'Pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5, 'Cheeky Spam': 4.5}
    print_menu(menu)
    order = get_order(menu)
    print('You ordered:',order)

main()