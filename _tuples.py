t=(1,2,3,4,5)
# type of constant list 
# Difference between list and tuple is that tuple cannot be modififed
# If we change any particular value in a tuple it will give error
# t[0]=5 # this is invalid 
print(t)

t1=(1,) # syntax if there is single element else it will be treated as integer 

t2=(1,2,3,4,1,1)
# to count occurance of an element 
print(t2)
no=t2.count(1)
print(no)

# it will return the first index of a number
ind=t2.index(2) # index of number 2 
print(ind)
