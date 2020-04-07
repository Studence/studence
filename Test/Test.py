from CommonCode.List.List import List

myList = List()
a = 0
for i in range(10):
    a = i
    myList.__append__(a)

myList.__print__()
print(myList.__getitem__(2))
