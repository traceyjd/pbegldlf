

pound_spam = open('pound_menu.txt', 'r')

    print('1st line:', pound_spam.readline())
    print('2nd line:', pound_spam.readline())
    #print(pound_spam.read())

    pound_spam.close()