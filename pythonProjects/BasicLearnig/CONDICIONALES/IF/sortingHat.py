print("Let's see who each of Harry Potter you belong to!")
print("Answer the following questions to see which house you belong to!")
slytherin = 0
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
message = ""

print("¿Do you like dawn or dusk?")
print("1. Dawn")
print("2. Dusk")

answer = int(input("Answer: "))

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    slytherin += 1
    hufflepuff += 1
else:
    print("Invalid input")

print("When I’m dead, I want people to remember me as:")
print("1. The Good")
print("2. The Great")
print("3. The Wise")
print("4. The Bold")

answer = int(input("Answer: "))

if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print("Invalid input")

print("Which kind of instrument most pleases your ear")
print("1. The violin")
print("2. The trumpet")
print("3. The piano")
print("4. The drum")

answer = int(input("Answer: "))
if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print("Invalid input")

if slytherin > gryffindor and slytherin > hufflepuff and slytherin > ravenclaw:
    message = "You belong to Slytherin!"
elif gryffindor > slytherin and gryffindor > hufflepuff and gryffindor > ravenclaw:
    message = "You belong to Gryffindor!"
elif hufflepuff > slytherin and hufflepuff > gryffindor and hufflepuff > ravenclaw:
    message = "You belong to Hufflepuff!"
elif ravenclaw > slytherin and ravenclaw > gryffindor and ravenclaw > hufflepuff:
    message = "You belong to Ravenclaw!"

print(message)