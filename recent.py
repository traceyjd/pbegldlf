
def average(numbers):
    total = 0
    for num in numbers:
        total = total + num

    avg = total/len(numbers)
    return avg

# main
# Use our function on prices
prices = [2.50, 3, 4.50, 5] #  First line of code thats run

result = average(prices)


print(result)