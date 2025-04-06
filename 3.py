# import json as j
# d='{"name":"anil","age":32}'
# z=j.loads(d)
# print(z['name'])
# print(z['age'])
# x={
#     'name':'vishnu',
#     'age':21
# }
# y=j.dumps(x)
# print(y)
# #regex
# import re
# str='rahul is sharing mohiddin room with vishnu'
# a=re.search('^rahul.*mohiddin.*vishnu$',str)
# if a:
#     print('there is a match')
# else:
#     print('there is no match')
# a=re.findall('rahul',str)
# print(a)
# z=re.search('\s',str)
# print(z)
# z=re.split('\s',str)
# print(re.sub('\s','|',str))
# import re
# patren=r'\d+'
# text='There are 123 apples 555'
# m=re.search(patren,text)
# if m:
#     print('match found',m.group())
# x=re.findall(patren,text)
# print(x)
# import re
# pattern=r'(\d+)-(\d+)-(\d+)'
# text='the event is on 2025-02-01'
# match=re.search(pattern,text)
# if match:
#     print('year:',match.group(1))
#     print('month:',match.group(2))
#     print('date:',match.group(3))
# #email validation using regular expression
# import re
# email_patrn=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}'
# str='pardha2002%+@gmai-.com is working mail id'
# match=re.search(email_patrn,str)
# if match:
#     print('email found',match.group())
##logging
# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('hello, debug')
# logging.info('hello, info')
# logging.warning('hello warning')
# logging.error('hello error')
# logging.critical('hello critical')
##logging sample
# import logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='app.log',
#     filemode='a',
#     format='%(name)s - %(levelname)s- %(message)s'
#    )
# logging.debug('hello, debug')
# logging.info('hello, info')
# logging.warning('hello warning')
# logging.error('hello error')
# logging.critical('hello critical')
##pylint
# for i in  range(20):
#     print(n)
'''
c - convention
'''
#exception 
# try:
#     x=10/0
# except ZeroDivisionError:
#     print('divide by zero')
# finally:
#     print('completed execution')
# # multiple Exception
# try:
#     num=int(input())
#     result=10/num
# except ValueError:
#     print('invalid input')
# except ZeroDivisionError:
#     print('cant divided by zero')
# except Exception as e:
#     print('unkown',e)
# else:
#     print('result',result)
# finally:
#     print('code executed')
# # user defined Exception
# def checkagte(age):
#     if age<18:
#         raise ValueError('age must be 18')
#     else:
#         print('ur eligible')
# try:
#     checkagte(int(input()))
# except ValueError as e:
#     print(e)
# #userdefined user not found exception
# class noteligibletovote(Exception):
#     pass
# def checkage(age):
#     if age<18:
#         raise noteligibletovote('age must be 18')
#     else:
#         print('yor are eligible')
# try:
#     checkage(int(input()))
# except noteligibletovote as e:
#     print(e)
##file handling
# file=open('C:/Users/unkown/Desktop/revature/vishnu/text.txt','r')
# c=file.read()
# print(c)
# c1=file.readline()
# c2=file.readlines()
# print(c1,c2,sep="\n")
# file=open('C:/Users/unkown/Desktop/revature/vishnu/text.txt','a')
# file.write('addding 4th line\n')
# file.write('adding 5th line')
# # a=file.read()
# # print(a)
# file.close()
# #file is existing or not??
# import os
# if os.path.exists("C:/Users/unkown/Desktop/revature/vishnu/text.txt"):
#     with open('C:/Users/unkown/Desktop/revature/vishnu/text.txt','r') as file:
#         content=file.read()
#         print(content)
# else:
#     print("file does not exist")
# #file handling with exceptional handling
# import os
# try:
#     with open('C:/Users/unkown/Desktop/revature/vishnu/text.txt','r') as file:
#         data=file.read()
#     with open('C:/Users/unkown/Desktop/revature/vishnu/text1.txt','w') as file1:
#         file1.write(data)
# except FileNotFoundError:
#     print('i/o or o/p operation file')
# except IOError as e:
#     print('io error',e)
# except Exception as e:
#     print('un expected')
# deleting file
# import os
# os.rmdir('C:/Users/unkown/Desktop/revature/vishnu/sample')
