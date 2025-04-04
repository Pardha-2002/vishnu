# #lambada function
# s1='hello good morning '
# s2=lambda func:func.upper()
# print(s2(s1))
# n= lambda x:"positive" if x>0 else "negative" if x<0 else "zero"
# print(n(0))
# print(n(-1))
# print(n(5))
# sq=lambda x:x**2
# print(sq(256))
# l1=[lambda arg= x:arg*10 for x in range(1,10)]
# for i in l1:
#     print(i(),end=' ')
# #even or odd
# fj=lambda x: 'even' if x%2==0 else 'odd'
# print(fj(5))
# print(fj(6))
# #lambda with multiple statements
# add_mul=lambda x,y:(x+y,x*y)
# print(add_mul(4,5))
# #lambda with filter
# n=[223,234,453,545,23,334]
# even=filter(lambda x:x%2==0,n)
# print(list(even))
# #lambda with map function
# a=[1,2,3,4,56]
# b=map(lambda x:x*2,a)
# print(list(b))
# #reduce funtion with lambda
# from functools import reduce
# a=[1,2,3,4,5]
# b=reduce(lambda x,y:x*y,a)
# print(b)
# #string format
# name='vishnu'
# age=22
# print('my name is {0} and my age is {1}'.format(name,age))
# print('my name is {} and my age is {}'.format(name,age))
# print(f'my name is {name} and my age is {age}')
# #inner function
# def fun1(msg):
#     def fun2():
#         print(msg)
#     fun2()
# fun1('hello')
# #decorator function
# def vishnu(func):
#     def rahool():
#         print('befor')
#         func()
#         print('after')
#     return rahool
# @vishnu #decorator
# def sample():
#     print('in sample')
# sample()
# import inspect
# print(inspect.signature(vishnu))
# #creating the class
# class human:
#     sound='we usually talk in multiple languages'
# human1=human()
# print(human1.sound)
# class dog:
#     spec='basic breed'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# # d1=dog()        
# d1=dog('candy',3)
# print(d1.name,d1.spec)
# ''' self paramaters refer to the the current instance of the class
# it allows us to access the attributes and methods of the object'''
# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
# d1=Dog('candy',10)
# d2=Dog('cheechu',12)
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
        