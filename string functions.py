a="bhavya is goodies"

# Length of a string
print(len(a))

# to check if string "a" ends with a given a character or a string
# it returns true or false 
print(a.endswith("goodies")) 
print(a.endswith("abc"))

# To count occurence of an alphabet or a string
print(a.count("o"))
print(a.count("zz"))
print(a.count("is"))

# To capitalise the first element of a string 
print(a.capitalize())

# to find an occurance of an string not a letter 
# and to return its first index 
# if that word appears more than once ! only first occurance is considered 
print(a.find("is"))

# to replace an old word with a new word in the whole string
print(a.replace("is","is too"))
print(a.replace("b","z"))

# IMP NOTE
# ANY CHANGES LIKE REPLACE IF NOT PRINTED WILL HAVE TO BE STORED IN THAT LETTER BY MODIFICATION 
a=a.replace("b","z")