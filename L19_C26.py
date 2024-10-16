a = [10,20,30,40,50]
print(a)
print("=============1=============")

index = 0
n = len(a)
print("Length:",n)
print("=============2=============")

while index < n:
    print(a[index], end = "  ")
    index = index + 1
print()
print("=============3=============")

for x in a:
    print(x, end = "  ")
print()
print("=============4=============")

sum = 0
for x in a:
    sum += x
print("Summation: " + str(sum))
print("=============+=============")

for i in range(0, n):
    print(str(i + 1) + ". " + str(a[i]))
print()