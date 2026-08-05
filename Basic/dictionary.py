#Accessing values in dictionary
dict1={ 1:'one',2:'two',3:'three' }
print('dictionary 1 : ',dict1)
#deleting values in dictionary
del dict1[1]
print('after deleting 1st element dictionary 1 : ',dict1)
dict1.pop(3)
print('after deleting 1st element dictionary 1 : ',dict1)
dict1.clear()
print('after clearing dictionary 1 : ',dict1)
# updating dictionary
dict1={1:'one',2:'two',3:'three' }
print('dictionary 1 : ',dict1)
dict1[1]='Ten'
print('after updating 1st element dictionary 1 : ',dict1)
# Basic dictionary operations
dict1={1:'one',2:'two',3:'three' }
print('dictionary 1 : ',dict1)
# Adding Element in dictionary
dict1[4]='Ten'
print('after Adaing element dictionary 1 : ',dict1)
#Merging of the dictionary | operater is used
dict2={4:'four',5:'five',6:'six',7:'seven'}
print('dictionary 2 : ',dict2)
print('Merging of Two dictionary dict1 dict2 ',dict1|dict2)
# in built dictionaries functions.--> copy(),clear(),keys(),values(),update(),items(),pop(),poitem(),get()
dict1={1:'one',2:'two',3:'three' }
dict3=dict1.copy()
print('After copying dict1 to dictionary 3 : ',dict3)
dict3.clear()
print('After clearing Dictionary 3 : ',dict3)
print('Keys of the dict1 : ',dict1.keys())
print('Values of the dict1 : ',dict1.values())
dict2={4:'four',5:'five',6:'six',7:'seven'}
dict1.update(dict2)
print('After updating the  dict2 to dictionary 1 : ',dict1)
print('item of the dictionary 1',dict1.items())
dict1.pop(7)
print('after poping the element at last 7 th position of the dictionary 1 : ',dict1)
print(dict1.popitem())       # poping the last element and return values
print('Fifth key value of dictionary is  ',dict1.get(5))