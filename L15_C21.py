"""
i = 1
sum = 0
while i <= 5:
    sum =sum + i
    i = i + 1
print(sum)
"""

'''
n = int(input("Enter the last term: "))
sum = 0
i = 1
while i <= n :
    sum = sum + i
    i = i + 1
print(sum)
'''


#2+4+6+......+n
'''n = int(input("Enter the last term: "))
summ = 0
i = 2
while i <= n :
    summ = summ + i
    i = i + 2
print(summ)
'''

first = int(input("Enter the first term: "))
last = int(input("Enter the last term: "))
d = int(input("Enter the common difference: "))
summation = 0
i = first
while i <= last:
    print(summation ,"+", i, "=", summation + i)
    summation += i
    i += d
print("Summation:", summation)