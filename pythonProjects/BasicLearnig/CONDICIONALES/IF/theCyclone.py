print("Let's see if you meet the requirements to enter the cyclone")

height = int(input("Enter your height in CM: "))
credits = int(input("Enter the number of credits you have: "))
message = ""

if height < 132 and credits < 10:
    message = "Sorry, you are too short and do not have enough credits to ride the cyclone"

elif credits < 10:
    message = "Sorry, you do not have enough credits to ride the cyclone"

elif height < 132:
    message = "Sorry, you are too short to ride the cyclone"

elif height >= 132 and credits >= 10:
    message = "You can ride the cyclone!"

print(message)



