#tuples r collection data type like list, lists are larger than tuples also tuples are quicker to make
mytuple = ("max", 24, "boston")
print(mytuple)

item = mytuple[2]
print(item)

for i in mytuple :
 print(i)

mylist = list(mytuple)#convert tuple into a list which can be moded
print(mylist)

mytuole2 = tuple(mylist)#convert list to a tuple

i1 ,*i2,i3 = mytuole2 #use * to include a list in syntax

print(i2)
print(i3)