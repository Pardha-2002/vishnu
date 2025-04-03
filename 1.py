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
#if else statement
a=int(input())
b=int(input())

if a>b:
    print('a is greater than b')
elif a<b:
    print('b is greater than a')
else:
    print('a==b')
# nestedifelse
i=int(input())
if i!=0:
    if i>0:
        print('postive')
    else:
        print("negative")
else:
    print('i is 0')


n=5
while n>=0:
    if n==2:
        break
    print(n)
    n-=1
# for loop
thistuple=('apple','banana','cherry')
for x in thistuple:
    print(x)
# nestedforloop
x=[1,2]
y=[4,5]
for i in x:
    for j in y:
        print(i,j)
dict1={1:'rahool',2:'ravi',3:'kumar'}
for i in dict1.keys():
    print(i)
# function creating
def greet(name):
    print('hello',name)
greet('vishnu')
#return sum
def sum(a,b):
    return a+b
print(sum(1,2))
# default perameter
def greet(name='guest'):
    print('hello',name)
greet()
greet('bob')
#multiple return value
def get_details(name='basha',age=23):
    return name,age
n1,a1=get_details()
n2,a2=get_details('vishnu',22)
print(f"name:{n1} age :{a1}")
print(f"name:{n2} age :{a2}")
#function with *args
def add_all(*num):
    return sum(num)
print(add_all(1,2,34,5,6))
# function with keyword argumets **kwargs
def info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
info(name='vishnu',age=22,company='techm')
import array
fruits=array.array('u','applebanancherry')
print(fruits[0])
for i in fruits:
    print(i,end='')
print()
import array
num=array.array('i',[5,2,3,4,1])# if use u in the place of i we get type error
print(len(num))
print(sorted(num))
