f=open('sample.txt','r+')
# r : read mode
# w : write mode
# a : append mode
# r+ : read and write mode 
# rb: read in binary mode

f.write("Let's Learn File Handling")

data=f.read() # read the file
data=f.read(5) # reads the first 5 characters in the file 

# readline function reads every line of the text one by one
# reads the first line
data=f.readline()
print(data)
# reads the next line
data=f.readline()
print(data)
f.close()