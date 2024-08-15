import random

print("Vamos a simular el juego de casino Craps!")

gameOn = True
point = 0


def rollDices() -> int:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("Tirando los dados...")
    print("Dado 1: ", die1)
    print("Dado 2: ", die2)
    print("Total: ", die1 + die2)
    return die1 + die2


result = rollDices()

if result in [7, 11]:
    print("Ganaste! en el primer tiro")
    print("-----------------------------")
    gameOn = False
elif result in [2, 3, 12]:
    print("Perdiste! en el primer tiro")
    print("-----------------------------")
    gameOn = False
else:
    point = result
    print("Tu punto es: ", point)
    print("-----------------------------")

while gameOn:
    result = rollDices()
    if result == point:
        print("Sacaste ", result, "Ganaste!")
        print("-----------------------------")
        gameOn = False
    elif result == 7:
        print("Sacaste ", result, "Perdiste!")
        print("-----------------------------")
        gameOn = False
    else:
        print("Sacaste ", result, " sigues lazando...")
        print("-----------------------------")

print("Gracias por jugar!")
