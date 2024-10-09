# Odd Even

num = int (input("Enter a number: "))

if num == 0:
    print("The number you entered is Zero")

elif num % 2 == 0:
    print(num, "is an Even number.")

else:
    print(num, "is an Odd number.")
    # print(str(num) + " is an Odd number.")  #string concatenation
    # print(f"{num} is an odd number")     # formatted string
