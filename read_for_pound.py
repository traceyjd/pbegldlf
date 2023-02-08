
def read_pound_menu():
    pound_spam = open('pound_menu.txt', 'r')

    pound_menu = []
    for line in pound_spam:
        line = line.strip()     # This will strip white space including new line characters
        pound_menu.append(line)

    print(pound_menu)
    pound_spam.close()
