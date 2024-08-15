print("Let's to calculate the PH of a pool")

pH = float(input("Enter the PH level of the pool "))
if pH < 7.0:
    print("The pool is acidic")
elif pH > 7.0:
    print("The pool is basic")
else:
    print("The pool is neutral")
