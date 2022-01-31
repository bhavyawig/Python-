def percent(marks,n):
    return sum(marks)/n

a=int(input())
marks1=[]
for i in range(0,a):
    b=int(input())
    marks1.append(b)
length=len(marks1)
percentage=percent(marks1,length)
print(percentage)