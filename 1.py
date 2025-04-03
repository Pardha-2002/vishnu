str='vishnu is my name'
print(type(str))
print(str[1])
print(str[2])
print(str[-1])
# create a list and accessing
l=[1,2,3,4,5]
mixedd=['vishnu',1,'rahool',2,'basha',3,'rohit',4]
print(l,mixedd)
l=l+[4]
print(mixedd[1:3])
# print(l[-6])#array index out of bound
tup1=(1,2,3,4,5)
print(tup1[1])
print(tup1[2])
print(tup1[-1])
#boolean
a=True
b=False
print(type(a))
print(type(b))
print(type(True))
#set
s1=set('hellowelcomehello')
s2=set(['hello','for','hello'])
print('output',s1)
print('output2',s2)
#slicing
name='vishnu'
print(name[1])
print(name[1:4])
print(name.upper())
#range function
l=range(1,10,2)
print(list(l))
#fozen set
fs=frozenset({1,2,3})
# fs.add(4) attribute error
#dictionary
d1={'name':'vishnu','age':22,'company':'TechM'}
print(d1['name'])
#BINARY DATA TYPES
c=[65,66,67]
b=bytes([65])
print(b,c)
#NoneType
x=None
print(type(x))
# y
# print(type(y))
