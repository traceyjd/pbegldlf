
def read_pound_menu():
    pound_spam = open('pound_menu.txt', 'r')

    for line in pound_spam:
        print(line)

    pound_spam.close()
