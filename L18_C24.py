'''subjects = ["A", "B", "C", "D", "E"]
print(len(subjects))

subjects.append("F")
print(subjects)

subjects.insert(2, "b")
print(subjects)

subjects.remove("b")
print(subjects)'''

subjects = ["B", "D", "a", "C", "A", "c", "b", 'd' ]
subjects.sort()
print(subjects)

subjects.pop()
subjects.pop()
print(subjects)

'''subjects.clear()
print(subjects)'''

subjects2 = subjects.copy()
print(subjects2)

subjects3 = [30,50,20,40,20,20,20]
pos = subjects3.index(40)
print(pos)

a = subjects3.count(20)
print(a)
