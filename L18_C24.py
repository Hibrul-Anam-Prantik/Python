subjects = ["A", "B", "C", "D", "E"]
print("Array:", subjects)
print("Length:",len(subjects))
print("=============1=============")

subjects.append("F")
print("Updated Array:",subjects)
print("Updated Length:",len(subjects))
print("=============2=============")

subjects.insert(2, "b")
print("Updated Array:",subjects)
print("Updated Length:",len(subjects))
print("=============3=============")

subjects.remove("b")
print("Updated Array:",subjects)
print("Updated Length:",len(subjects))
print("=============4=============")

subjects = ["B", "D", "a", "C", "A", "c", "b", 'd' ]
subjects.sort()
print("\nNew Sorted Array:",subjects)
print("Length:",len(subjects))
print("=============5=============")

subjects.pop()
print("Updated Array:",subjects)
print("Updated Length:",len(subjects))
print("=============6=============")

subjects.pop()
print("Updated Array:",subjects)
print("Updated Length:",len(subjects))
print("=============7=============")

'''subjects.clear()
print(subjects)'''

print("=============8=============")

subjects2 = subjects.copy()
print("Copied Array:",subjects2)
print("Length:",len(subjects))
print("=============9=============")

subjects3 = [30,50,20,40,20,20,20]
pos = subjects3.index(40)
print(pos)
print("=============X=============")

a = subjects3.count(20)
print(a)
