a=[1,2,3,1,9,6]

# u can update a list
a[0]=101

# to sort a list
a.sort()
print(a)

# to reverse a list
a.reverse()
print(a)

# to append an element at end (same as push_back)
a.append(34)
print(a)

# to insert an element at a given index
# syntax : list.insert(index,value)
a.insert(2,100)  # to insert an element at index 2 which is 100
print(a)

# to remove an element from a given position 
a.pop(2)
print(a)

# to remove an element with that value from list only in its first occurance 
a.remove(1)
print(a)