subjects = ["A", "B", "C", "D", "E"]
print(len(subjects))
print("=============================")

subjects.append("F")
print(subjects)
print("=============================")

subjects.insert(2, "b")
print(subjects)
print("=============================")

subjects.remove("b")
print(subjects)
print("=============================")

subjects = ["B", "D", "a", "C", "A", "c", "b", 'd' ]
subjects.sort()
print(subjects)
print("=============================")

subjects.pop()
print(subjects)
print("=============================")

subjects.pop()
print(subjects)
print("=============================")

'''subjects.clear()
print(subjects)'''
print("=============================")

subjects2 = subjects.copy()
print(subjects2)
print("=============================")

subjects3 = [30,50,20,40,20,20,20]
pos = subjects3.index(40)
print(pos)
print("=============================")

a = subjects3.count(20)
print(a)
