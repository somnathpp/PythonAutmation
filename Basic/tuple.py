#Basic Tuple Operartion
tup1=(1,2,3)
#Aceesing Tuple Values
print('Tuple 1 :',tup1)
tup2=(11,12,13)
print('Tuple 2 :',tup2)
#Acessing Tuple Values
print('Second Value of Tup1: ',tup1[1])
print('Third Value of Tup2: ',tup2[2])
#deleting Values from Tuple
temp1=list(tup1)
temp2=list(tup2)
temp1.pop(1)
temp2.pop(2)
print('After deleting 2nd Value from Tup1 :',tuple(temp1))
print('After deleting 3rd Value from Tup2 :',tuple(temp2))
#Updating Tuple
temp1[0]=10
temp2[0]=20
print('After updating 1st Value from Tup1 :',tuple(temp1))
print('After updating 1st Value from Tup2 :',tuple(temp2))
#tuple operations
print("Meging Two Tuple :",tup1+tup2)
print('slicing :',tup1[:2])
print('slicing :',tup1[2:])
#  function Tuple
print('length of tuple1:',len(tup1))
print('length of tuple2 :',len(tup2))
print('Min of tuple1:',min(tup1))
print('Max of tuple2 :',max(tup2))
print('Sum of tuple1:',sum(tup1))
print('Sum of tuple2 :',sum(tup2))