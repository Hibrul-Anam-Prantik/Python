"""
a = int(input("Obtained marks: "))

if a >= 80 and a <= 100:
    print("A+")
elif a >= 70 and a < 80:
    print("A")
elif a >= 60 and a < 70:
    print("A-")
"""

a = 50
if 80 <= a <= 100:
    print("A+")
elif 80 > a >= 70:
    print("A")
else:
    print("Lower than A")

a = 79
if 80 <= a <= 100:
    print("A+")
elif 70 <= a < 80:
    print("A-")
else:
    print("Lower than A")