'''
* Collections
* Os module & Datetime
* Math and Random
* Python Debugger
* Timeit
* Regular Expressions
* unzipping and zipping modules

'''


'''
/************************************************/
Collections
'''
print('\n******************* Collections ***************\n')

from collections import Counter
mylist = [1,1,1,1,1,1,2,2,2,2,7,7,7,7,7,7]
print (Counter(mylist))
print (type(Counter(mylist)))

mylist = ['a','a',20,20,20]
print (Counter(mylist))

print (Counter('aaaaaabbbbbbshshshshshjs'))

print('\n************************************************\n')

letters = 'aaaabbbbbbcccccccddddddd'
c = Counter(letters)
print(c)
print(c.most_common())
print(c.most_common(3))
print(list(c))

print('\n******************* defaultdict ***************\n')

from collections import defaultdict
d = defaultdict(lambda:0)
d['correct'] = 100
d['Working KEY!']
print(d)

print('\n************** namedtuple *********************\n')

mytuple = (10,20,30)
print(mytuple[0])

from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])

sammy = Dog(age=5,breed='Husky',name='Sammy')

print(type(sammy))

print(sammy.age)
print(sammy[0])

print('\n******************* Shutil and OS Modules ***************\n')
'''
Shutil and OS Modules
Opening and Reading Files and Folders
* open an individual file with Python
* open every file in a directory
* move files around on our computer

Python's OS module and Shutil allow us to easily navigate files and directories
on the computer and then perform actions on them (moving & deleting )
'''

f = open('practice.txt','w+')
f.write('This is a test string ')
f.close()

import os
print(f'the current directory is\t{os.getcwd()}')
print(f'List all directory\t{os.listdir()}')
print(f'List all directory\t{os.listdir("/Users/aelkhodary/Documents")}')

print('\n*********************************************\n')

import shutil
#help(shutil.move)
shutil.move('practice.txt','/Users/aelkhodary/Documents/GitHub/Python-Bootcamp')

'''
the os modules provides 3 methods for deleting files:
* os.unlik(path)
* os.rmdir(path)
* shutil.rmtree(path)

# All of these methods can not be reserved!
# Instead we will use the 'send2trash' module.A safer alternative that sends deleted
  files to the trash bin instead of permanent removal
# Install the send2trash module with
  >>pip install send2trash 'at your command line'

'''
import send2trash
send2trash.send2trash('/Users/aelkhodary/Documents/GitHub/Python-Bootcamp/practice.txt')


print('\n*********************************************\n')

'''
Iterate over folders and sub_folders

file_path = '/Users/aelkhodary/Documents/GitHub/Python-Bootcamp '
for folder , sub_folders , files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print('\n')
    print('The subfolders are : ')
    for sub_folder in sub_folders:
        print(f"\t Subfolder : {sub_folder}")

    print('\n')
    print('The files are : ')
    for f in files:
        print(f'\t File: {f}')
    print('\n')

'''
# q to exit the command
#print(help(os.walk))


print('\n******************* Datetime Module ***************\n')

import datetime
mytime = datetime.time(2)
print(mytime.microsecond)
print(mytime.second)
print(mytime.minute)
print(mytime.hour)
print(mytime)
print('\n**************  ***************\n')
mytime = datetime.time(13,20,1,20)
print(mytime.microsecond)
print(mytime.second)
print(mytime.minute)
print(mytime.hour)
print(mytime)
print('\n**************  ***************\n')
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime())
#from datetime import *
from datetime import datetime
mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)
print(mydatetime.replace(year=2020))
print('\n************** DATE **************\n')
from datetime import date
date1 = date(2021,11,3)
date2 = date(2020 ,11,3)
result = date1 - date2
print(type(result))
print(result)
print(result.days)
print('\n************** DATE TIME**************\n')
datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)
result = datetime1 - datetime2
print(type(result))
print(result)

print('\n******************* Math and Random Modules  ***************\n')

'''
import math
print(help(math))
'''
#from math import *
#print(frexp(2))

# this is the best option can use to import module
import math
print(math.floor(4.35))
print(math.ceil(4.35))
print(math.pi)
print(math.e)
print(math.log(math.e))
print(math.log(100,10)) # 10**2
print(math.sin(10))
print(math.degrees(math.pi/2))
print(math.radians(180))

print('\n********************  *********************\n')

from math import floor , ceil , pi
print(floor(4.35))
print(ceil(4.35))
print(pi)

print('\n************** Random **********************\n')

import random
print(random.randint(0,100))

random.seed(2)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))

# SAMPLE WITH REPLACEMENT
print(random.choices(population=mylist , k=10))

# SAMPLE WITHOUT REPLACEMENT
print(random.sample(population=mylist , k=10))

print(mylist)
random.shuffle(mylist)
print(mylist)

print(random.uniform(a=0 , b=100))
print(random.gauss(mu=0 , sigma=100))


print('\n******************* Python Debugger **********************\n')
'''
https://docs.python.org/3/library/pdb.html
'''

import pdb

x = [1,2,3]
y = 2
z = 3

result_one = y + z
#pdb.set_trace()
#result_two = y + x

print('\n************* Python Regular Expressions Part One ****************\n')

'''
https://docs.python.org/3/library/re.html

Phone Number
(555)-555-5555
Regex Pattern
r"(\d\d\d)-\d\d\d-\d\d\d\d"
r"(\d{3})-\d{3}-\d{4}"
r'/d' we tell python after comming / is regular expression

'''

text = "the agent's phone number is 408-555-1234. Call soon!"

print('phone' in text)

import re

pattern = 'phone'
res = re.search(pattern,text)
print(type(res))
print(res.span())
print(res.start())
print(res.end())

# None
print('\n****** None ********\n')
pattern = 'NOT IN TEXT'
res = re.search(pattern,text)
print(res)

# FIRST MATCH
print('\n******* FIRST MATCH *******\n')
pattern = 'phone'
text = "my phone once , my phone twice "
match = re.search(pattern,text)
print(match)
print(match.span())
print(match.group())

# FIND ALL
print('\n********* FIND ALL *******\n')
pattern = 'phone'
text = "my phone once , my phone twice "
matches = re.findall(pattern,text)
print(matches)
print(type(matches))
print(len(matches))


# FIND ITERATOR
print('\n********* FIND ITERATOR *******\n')
pattern = 'phone'
text = "my phone once , my phone twice "
for match in re.finditer(pattern,text):
    print(match)
    print(type(match))
    print(match.span())
    print(match.group())


print('\n********* Regular Expressions *******\n')
text = "My Phone number is 408-555-1287"
#pattern = "\d\d\d-\d\d\d-\d\d\d\d"
pattern = r"\d{3}-\d{3}-\d{4}"
print(type(pattern))
#match = re.search(r'\d{3}-\d{3}-\d{4}',text)
match = re.search(pattern,text)
print(match)
print(match.span())
print(match.group())

print('\n********* Regular Expressions Groups*******\n')
text = "My Phone number is 408-555-1287"
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
match = re.search(phone_pattern,text)
print(match.group())
print(match.group(1))
print(match.group(2))
print(match.group(3))

print('\n********* Additional Regex Syntax *******\n')

print('\n********* pipe operator -> that stands for or meaning *******')
match = re.search(r'cat|dog','The dog is here ')
print(match.group())
match = re.search(r'cat|dog','The cat is here ')
print(match.group())

print('\n********* wild card operator -> acts as placement that will match any character *******')
# WITHOUT WILD CARD
match = re.findall(r'at', 'The cat in the hat sat there')
print(match)
# WITH WILD CARD
match = re.findall(r'.at', 'The cat in the hat sat there')
print(match)
match = re.findall(r'...at', 'The cat in the hat went splat')
print(match)

print('\n********* starts with and ends with *******')
# START WITH
match = re.findall(r'^\d', '1 is a number ')
print(match)
'''
match = re.findall(r'^\d', 'The 1 is a number ')
print(match)
'''
# END WITH
match = re.findall(r'\d$', 'The number is 2')
print(match)

print('\n**************************************** Timing Your Python Code **********************')

'''
* Time your code's performance:
  - we will focus on 3 ways of doing this
   * simply tracking time elapsed  'الوقت المنقضي'
   * Using the timeit module
   * Special %%timeit "magic" for Jupyter Notebooks

'''
#  WE NEED TO KNOW WHICH ONE IS MORE EFFICIENT
def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    return list(map(str,range(n)))

print(func_one(10))

print('\n***************** Tracking time elapsed *******************')
# CURRENT TIME BEFORE
import time
start_time = time.time()
#RUN CODE
result = func_one(10)
#CURRENT TIME AFTER RUNNNING CODE
end_time = time.time()
#ELAPSED TIME
elapsed_time = end_time - start_time

print(f'elapsed_time  of function one is {elapsed_time} ')

# CURRENT TIME BEFORE
import time
start_time = time.time()
#RUN CODE
result = func_one(10)
#CURRENT TIME AFTER RUNNNING CODE
end_time = time.time()
#ELAPSED TIME
elapsed_time = end_time - start_time

print(f'elapsed_time  of function two is {elapsed_time} ')


print('\n***************** Using the timeit module *******************')

import timeit
# stmt is the acually code i want to run
stmt = '''
func_one(1000)
'''
# setup is essentially what code needs to be run before you call statement 'stmt'
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
# number is number of times you actually want to run this code
print(f'elapsed_time  of function one is {timeit.timeit(stmt,setup,number=100)} ')


stmt = '''
func_two(1000)
'''
setup = '''
def func_two(n):
    return [str(num) for num in range(n)]
'''
print(f'elapsed_time  of function two is {timeit.timeit(stmt,setup,number=100)} ')


print('\n***************** Special %%timeit "magic" for Jupyter Notebooks *******************')
'''
%%timeit
func_one(1000)

%%timeit
func_two(1000)
'''


print('\n**************************************** Zipping and unzipping files **********************')

'''
* Create a couple of text files for us to work with and compress
* How to zip individual files and compress them
'''

f = open('fileone.txt','w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt','w+')
f.write('TWO FILE')
f.close()

import zipfile
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('fileone.txt', compress_type = zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type = zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('extracted_content')
'''
Shell Utility library is abetter tool for archive an entire folder or extract them
'''
print('\n***************** Shell Utility library *******************')

import shutil
dir_to_zip = '/Users/aelkhodary/Documents/GitHub/Python-Bootcamp/section14/extracted_content'
output_filename = 'example'
shutil.make_archive(output_filename,'zip',dir_to_zip)
shutil.unpack_archive('example.zip','final_unzip','zip')

print('\n*****************  Advanced Python Module Puzzle *******************')
