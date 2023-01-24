# Comparing Lists

# How do we check if two lists are equal????
# They have to have the same items and in exactly the same order

my_list = [1, 2, 3, 4]
your_list = [4, 3, 2, 1]
his_lst = [1, 2, 3, 4]

print(my_list == your_list) # evaluates to false
print(my_list == his_lst) # evaluates to true

# Dictionaries are different as they can be in any order so if you have the same pairs they will return True as being the same

# Two Dimensional List - List of lists

menus = [ ['Spam n Eggs', 'Spam n Jam', 'Spam n Eggs'],
          ['SLT (Spam-Lettuce-Tomato', 'PB&S (PB&Spam)'],
          ['Spalad', 'Spamghetti', 'Spam Noodle Soup']]

print(menus)
print(menus[0][1]) # The list at index 0 in the outer list, then the item at index 1 in the inner list

#  If you want to see the items listed for Breakfast lunch and dinner we can use a Dictionary of Lists as below
menus = { 'Breakfast' : ['Spam n Eggs', 'Spam n Jam', 'Spam n Eggs'],
          'Lunch' : ['SLT (Spam-Lettuce-Tomato', 'PB&S (PB&Spam)'],
          'Dinner' : ['Spalad', 'Spamghetti', 'Spam Noodle Soup']}

print('Breakfast Menu:\t', menus['Breakfast'])
print('Lunch Menu:\t', menus['Lunch'])
print('Dinner Menu:\t', menus['Dinner'])



