'''n = input("NUmbers: ")
sum = 0
list = n.split()

for x in list:
    sum = sum + int(x)
print(sum)'''


"""number of words = now
number of letter = nol
number of digits = nod"""

nol = 0
nod = 0
now = 0
text = input("Enter the text here: ")

for x in text:
    x = x.lower()
    if 'z'>=x>='a':
        nol = nol + 1
    elif '9'>=x>='0':
        nod = nod + 1
    elif '9'>=x>='0':
        nod = nod + 1

print(nol)
print(nod)