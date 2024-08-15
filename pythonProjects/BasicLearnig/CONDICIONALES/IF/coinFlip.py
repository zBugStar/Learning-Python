import random
print("Coin Flip")
num = random.randint(0,1)

if num > 0.5:
    message = "Heads"
else:
    message = "Tails"

print("The coin landed on", message)



