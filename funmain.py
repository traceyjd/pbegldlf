
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
main()

