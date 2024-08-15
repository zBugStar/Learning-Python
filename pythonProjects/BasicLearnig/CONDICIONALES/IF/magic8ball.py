import random

print("Magic 8 Ball")
question = input("Ask me a question: ")
answer = random.randint(1, 9)
message = ""

if answer == 1:
    message = "Yes - definitely."
elif answer == 2:
    message = "It is decidedly so."
elif answer == 3:
    message = "Without a doubt."
elif answer == 4:
    message = "Reply hazy, try again."
elif answer == 5:
    message = "Ask again later."
elif answer == 6:
    message = "Better not tell you now."
elif answer == 7:
    message = "My sources say no."
elif answer == 8:
    message = "Outlook not so good."
elif answer == 9:
    message = "Very doubtful."

print("8 Ball magic: ", message)
print("Thank you for playing!")

