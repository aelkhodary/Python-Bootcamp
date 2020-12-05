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

print('\n**************  **************\n')

from math import floor , ceil , pi
print(floor(4.35))
print(ceil(4.35))
print(pi)

print('\n************** Random **************\n')

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
