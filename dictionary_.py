# This is similar to maps in c++|| syntax : dict(key,value)
dict={
    "bhavya":"good",
    69:"too good",
    "more":[1,2,3,4],
    "less":["mine","forever",1],
}
print(dict.keys()) # print only key 
print(dict.values()) # print only value
print(dict.items()) # print pairs

print(dict.get("69")) #returns value of the given key 
print(dict.get[69])

print(dict.get("9")) # this will return none and not give error
print(dict.get[9])   # this will give error 

