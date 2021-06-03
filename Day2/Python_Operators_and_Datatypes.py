#This is a comment
#variable
n1=10
n2,name=10.5,'Hetal'
n3=n4=2
print(n1)
print(n2)
print(name)
print("n2 is",n2)
print("n3 is",n3,"n4 is",n4)

#type isinstance
n1=10
print(n1,"is of type",type(n1))
n2=10.2
print(n2,"is type of",type(n2))
print(n2,"is complex number",isinstance(10.5, int))

#datatype
#list
l=['hello',34,34.5,12]
print(l)
print("l[2] is : " ,l[2])
print("l[-1:] is : "  ,l[-1:])
print("l[1:3] is : ",l[1:3])

#tuple
t=("hello","world",23,78)
print(t)
print("t[2] : ",t[2])
print("t[2:3] : ",t[2:])

#dictionary
d={1:"hello",2:"world","key":10}
print(d)
print('d[2]=',d[2])

mydict={}
num=int(input("Enter the numbers:"))
for totnum in (0,num):
    a,b=input("Enter key value pair: ").split(",")
    if a in mydict:
        mydict[a].append(b)
    else:
        mydict[a]=[b]
print(mydict)







