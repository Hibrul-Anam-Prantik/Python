# cgpa checker

mark = float(input("Obtained Mark: "))
if mark >= 90:
    cg = 4.00
elif mark >= 85:
    cg = 3.70
elif mark >= 80:
    cg = 3.30
elif mark >= 75:
    cg = 3.00
elif mark >= 70:
    cg = 2.70
elif mark >= 65:
    cg = 2.30
elif mark >= 60:
    cg = 2.00
elif mark >= 55:
    cg = 1.70
else:
    cg = 1.30

print("You got CG " + str(cg))