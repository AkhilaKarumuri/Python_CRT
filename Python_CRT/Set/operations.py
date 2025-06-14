Set={10,20,30,40,50,60,60}
print(Set)
print(type(Set))
for i in Set:
    print(i)
print(10 in Set)
#add
Set.add(70)
print(Set)
#update
Set.update({80,90})
print(Set)
#remove
Set.remove(10)
print(Set)
#POP
Set.pop()
print(Set)
#discard
Set.discard(20)
print(Set)
#Clear
Set.clear()
print(Set)
#Union
set1={1,2,3,4}
set2={5,6,7,8}
print(set1|set2)
#intersction
print(set1&set2)
#Difference
print(set1-set2)
#Absolute Difference
print(set1^set2)
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))