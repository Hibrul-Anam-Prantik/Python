a = 120
b = 10
c = 80
if a > b and a > c:
    print(str(a) + " is Max.")
elif b > a and b > c:
    print(str(b) + " is Max.")
else:
    print(c, "is Max.")
X = input("Enter a letter (LowerClass): ")
if X == "a" or X== "e" or X=="i" or X=="o"or X=="u":
    print("Vowel.")
else:
    print("Consonant.")