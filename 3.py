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




