#!/usr/bin/python3
import random
number = random.randint(-10, 10)
import random
# Generate a random signed number
number = random.randint(-10, 10)

# Print the generated number
print(f"{number} ", end="")

# Check whether the number is positive, negative, or zero
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")

