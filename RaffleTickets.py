
#  Generate Raffle Tickets

import random

r1 = random.random()  # Gives us a number from [0.0, 1.0]
print(r1)

r2 = random.choice([1,2,3,4,5]) # Gives us a number between 1 & 5 from our list
print(r2)

r3 = random.randint(1, 1000) # Gives us a random number in this range
print(r3)                    # This will allow us to picka random raffle ticket from 1-1000

