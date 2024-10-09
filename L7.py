# Largest Number

num1 = input("Enter a number, \na = ")
num2 = input("Enter a number,\nb = ")

if num1 > num2:
    print("a is largest [a = ", num1, "]")
elif num1 < num2:
    print("b is largest [b = " + num2 + "]")
else:
    print("a & b are same [a = ", num1, ", b = " + num2, "]")
