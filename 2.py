#lambada function
s1='hello good morning '
s2=lambda func:func.upper()
print(s2(s1))
n= lambda x:"positive" if x>0 else "negative" if x<0 else "zero"
print(n(0))
print(n(-1))
print(n(5))
sq=lambda x:x**2
print(sq(256))
l1=[lambda arg= x:arg*10 for x in range(1,10)]
for i in l1:
    print(i(),end=' ')
#even or odd
fj=lambda x: 'even' if x%2==0 else 'odd'
print(fj(5))
print(fj(6))
#lambda with multiple statements
add_mul=lambda x,y:(x+y,x*y)
print(add_mul(4,5))
#lambda with filter
n=[223,234,453,545,23,334]
even=filter(lambda x:x%2==0,n)
print(list(even))
#lambda with map function
a=[1,2,3,4,56]
b=map(lambda x:x*2,a)
print(list(b))
#reduce funtion with lambda
from functools import reduce
a=[1,2,3,4,5]
b=reduce(lambda x,y:x*y,a)
print(b)
#string format
name='vishnu'
age=22
print('my name is {0} and my age is {1}'.format(name,age))
print('my name is {} and my age is {}'.format(name,age))
print(f'my name is {name} and my age is {age}')
#inner function
def fun1(msg):
    def fun2():
        print(msg)
    fun2()
fun1('hello')
#decorator function
def vishnu(func):
    def rahool():
        print('befor')
        func()
        print('after')
    return rahool
@vishnu #decorator
def sample():
    print('in sample')
sample()
import inspect
print(inspect.signature(vishnu))
#creating the class
class human:
    sound='we usually talk in multiple languages'
human1=human()
print(human1.sound)
class dog:
    spec='basic breed'
    def __init__(self,name,age):
        self.name=name
        self.age=age
# d1=dog()        
d1=dog('candy',3)
print(d1.name,d1.spec)
''' self paramaters refer to the the current instance of the class
it allows us to access the attributes and methods of the object'''
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'{self.name} is {self.age} years old'
d1=Dog('candy',10)
d2=Dog('cheechu',12)
# print(d1,d2,sep='\n')
class Dog:
    spec='canine'
    def __init__(self,name,age):
        self.name=name
        self.age=age
d1=Dog('buddy',3)
d2=Dog('charlie',2)
print(d1.spec)
print(d1.name)
print(d2.name)
d1.name='max'
print(d1.name)
d1.spec='fenile'
print(d1.spec)
print(d1.spec)
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError('subcasses must implement this menthod')
class dog(Animal):
    def sound(self):
        return 'woof!'
a=Animal('generic animal')
d=dog('buddy')
print(a.name)
print(d.name)
print(d.sound())
#inner class
class color:
    def __init__(self,name):
        self.name=name
        self.lg=self.lightgreen()
    def show(self):
        print(f'name:{self.name}')
    class lightgreen:
        def __init__(self):
            self.name='light green'
            self.code='024avc'
        def display(self):
            print(f"name:{self.name}")
            print(f"code:{self.code}")
outer =color('green')
outer.show()
inner=outer.lg
inner.display()
#remote without battery
#college without department
#super keyword also method overriding example
class parent:
    def show(self):
        print("inside parent")
class child(parent):
    def show(self):
        super().show()
        print('inside child')
obj=child()
obj.show()
# pulbic protected private 
class private:
    def __init__(self):
        self._salary=50000
        self.__pf=25000
    def salary(self):
        print(self.__pf)
        return self._salary
obj=private()
print(obj.salary())
print(obj._salary)
#iterator
numbers=[1,2,3,4,5,6]
iter_numbers=iter(numbers)
for i in range(len(numbers)):
    print(next(iter_numbers))
#local scope
def myfun():
    x=200
    print(x)
myfun()
#enclosing scope
def myfunc():
    x=200
    def myc():
        print(x)
myfun()
#global scope
x=200
def myfunc():
    print(x)
myfun()
print(x)
#importing the modules
import sample
print(sample.add(1,2))
print(sample.sub(3,1))
# math functions
import math
print(math.pow(5,3))
print(math.floor(4.3))
print(math.sqrt(5))
print(math.factorial(5))
print(math.tan(45))
print(math.pi)
print(math.ceil(5.4))
# numpy importing
import numpy as np
arr=np.array([1,2,3])
brr=np.array([4,5,6])
print(arr)
print(type(arr))
a=np.zeros((2,3))
b=np.ones((3,2))
c=np.arange(0,10,2)
d=np.linspace(0,1,5)
e=np.random.rand(2,2)
print(a,b,c,d,e,sep='\n')
print(arr+brr)
print(brr-arr)
print(arr*brr)
print(arr**2)
#multidimensional array
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[2,0],[1,3]])
print(np.dot(a,b))
print(np.transpose(a))
print(np.linalg.inv(a))
arr=np.array([[10,20,30],[40,50,60]])
print(arr[0,1])
print(arr[:,1])
print(arr[1])
arr=np.array([1,2,3,4])
print(arr.mean())
print(arr.sum())
print(arr.std())
print(arr.max())
print(arr.min())
#pandas
import pandas as pd
s= pd.Series([10,20,30,40],index=['a','b','c','d'])
print(s)
# pandas dataframes
import pandas as pd
data={
    "name":['bob','john','mishra'],
    "age":[36,46,56],
    "city":['banglore','vijayawada','chennai']
}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)
print(df['age'])
print(df[['name','city']])
print(df[df['age']>36])
df['age']+=1
df['country']='usa'
df.rename(columns={'age':'years'}, inplace=True)
df.drop('city',axis=1)
print(df)