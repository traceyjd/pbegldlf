
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


