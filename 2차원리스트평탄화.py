listA = [1,2,[3,4],5,[6,7],[8,9]]
listB = []
for i in listA:
    if type(i) == list:
        listB.extend(i)
    else:
        listB.append(i)
print(listB)
