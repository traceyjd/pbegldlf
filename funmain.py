
def average(numbers):
    total = 0
    for num in numbers:
        total = total + num

    avg = total/len(numbers)
    return avg

# Use our function on prices

def main():
    prices = [2.50, 3, 4.50, 5]  # First line of code thats run

    result = average(prices)

    print(result)
main() #  All of the execution starts here and will run the main function above. It will run all the lines of code in
# in main until average gets called above, then average runs and returns a value to main and main continues

#  Functions dont get run until they are called


# Scope local and global scope, if we name variables inside a funtion they will run only in that function
# If we name variables outside the function they can be used globally
# Remember you cant name variables after the main program as main will be run first and wont know about it
# So watch out for nameerrors as these may indicate scope

