#1 + 2 + 3 + ... + n
n = int(input("Enter the last digit: "))
sum = 0
for x in range(1, n + 1, 1):
    sum = sum + x
print(sum)
print("========================")

#2 + 4 + 6 + ... + n
n = int(input("Enter the last digit: "))
sum = 0
for x in range(2, n + 1, 2):
    sum = sum + x
print(sum)
print("========================")

#1^2 + 2^2 + 3^2 + ... + n^2
n = int(input("Enter the last digit: "))
sum = 0
for x in range(1, n + 1, 1):
    sum = sum + x**2
print(sum)
print("========================")

#1 x 2 x 3 x ... x n
import math
n = int(input("Enter the last digit: "))
product = 1
for x in range(1, n+1, 1):
    product = product * x
print(product)
print("========================")





