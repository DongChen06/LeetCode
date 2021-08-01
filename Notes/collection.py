import collections


myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

newList = collections.Counter(myList)

print(newList)
print(newList.keys())
print(list(newList.keys())[0])
print(newList.values())