mylist = ["banan", "apple", "vinegar",]
print (mylist)
mylist2 = list()
print(mylist2)
item= mylist[2]
print(item)



print(mylist)

print(len(mylist)) #len is the length method

mylist.append("lemonade") #append to the last index
print(mylist)

mylist.insert(1,"bluebery") #put item in a specific index

print(mylist)
item =mylist.pop() #pop() used to take the last item from list
print(item)

mylist.remove("banan") #remove(an item)
print(mylist)

mylist.reverse( ) #revers order
print(mylist)

#mylist.sort() #sort from smallest to biggest
print(mylist)

newlist = sorted(mylist) #to creat a new list without messing the old one
print (newlist)

nlist = [0] *5 #print list with 5 zeros
print(nlist)

mlist = mylist + nlist # you can add lists
print(mlist)

a = mlist[1:4] # creates a new list a that is sliced form mlist
print(a)

a = mlist[::2] #from first to start and taking the second number
print(a)

l = a.copy() #creates a l a copy of a without making l refer to same memory segment as in a