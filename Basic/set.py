#Creating Set
set1={1,2,3}
set2={4,5,6}
print('Set1 :',set1)
print('Set2 :',set2)
#Accessing Values in Set can possible through the looping or iteration
set3={'Orange','Apple','Papaya','Mango'}
print('Set3 :',set3)
for item in set3:
    print(item)
#  deleting values in set
set3.discard('Apple')  # discard() doent throw error when item doesnt exist but remove() throw error message
print('After Discarding Apple From set3',set3)
#  updating sets
set4={'Orange','Apple','Papaya','Mango'}
print('Before Updating  set4 : ',set4)
lst1=['Pineapple','Dragon Fruit','Kiwi']
set4.update(lst1)
print('After Updating set4 : ',set4)
# Opertation on The set
# Set Union
setA={1,2,3}
setB={3,4,5,6}
print(f'setA : {setA}  setB : {setB}')
print('Union of setA and setB : ',setA.union(setB))  # set union can also do with | operater
print('Intersection of setA and setB : ',setA.intersection(setB))  # set intersection can also do with & operater
print('Difference of setA and setB : ',setA.difference(setB))  #set difference can also do with - operater ex A-B
print('Difference of setB and setA : ',setB.difference(setA)) #set difference can also do with - operater ex A-B
# Function in the set
'''
Method	                                    Description
add(elem)	                                Adds a single element to the set.
update(iterable, ...)	                    Adds multiple elements from iterables to the set.
remove(elem)	                            Removes an element; raises KeyError if not found.
discard(elem)	                            Removes an element if present; no error if not found.
pop()	                                    Removes and returns an arbitrary element; raises KeyError if empty.
clear()
'''