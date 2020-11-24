print("hello world")
a=10
a=a+a
print(a)
a='ali'
print(type(a))
print("Hello world"[8])
x = "Hello World"
print(x.upper())

print('The {} {} {}'.format('fox','brown','quick'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {0} {0} {0}'.format('fox','brown','quick'))
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))
#Float formatting follows "{value:width.precision f}"
result=100/777
print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))

# f string new in bython 3.6
name="Ali"
print(f'Hello ,his name is {name}')
 #*****************************************************************#
# Tuples with pithon it's similare to lists but it is immutability
t1 =(1,2,3)
print(t1)
t2=('one',2)
print(t2)
print(t2[0])
print(t2[-1])   #last item
t2=('a','a','b')
print(t2.count('a'))
print(t2.index('a')) #return first index
#t2[0]='NEW' #TypeError: 'tuple' object does not support item assignment
 #*****************************************************************#
# Sets are unordered collection of unique elements
myset = set()
myset.add(1);
print(myset)
myset.add(2);
print(myset)
myset.add(2);
print(myset)
myList = [1,1,1,1,1,1,1,1,2,2,2,2,3,3]
myset= set(myList)
print(myset)

# Booleans in Python
ty = type(True)
print(ty)
ty = type(False)
print(ty)
print(1>2)
print(1==1)
 #*****************************************************************#
# I/O with Basic Files in Python
myfile = open('myfile.txt') # file directory is save in the same location
# myfile = open('myfile1.txt') FileNotFoundError: [Errno 2] No such file or directory: 'myfile1.txt'
str = myfile.read();
print(str)

str = myfile.read();
print(str) # this will return ''
myfile.seek(0) # retun back the cursore to the first line
str = myfile.read();
print(str)

myfile.seek(0) # retun back the cursore to the first line
str = myfile.readlines(); #retun list of lines
print(str)
myfile.close()
# insted of 1-myfile.seek(0) & 2-myfile.close()
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
print(contents)

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
print(contents)

# with open('myfile.txt',mode='w') as new_file: #io.UnsupportedOperation: not readable
    #contents = new_file.read()
#print(contents)

#with open('myfile.txt',mode='w') as new_file:
    #contents = new_file.read()
#print(contents)

with open('myfile.txt',mode='w') as f:
    f.write('Hello World')
    f.close()

#******************************************************************************#
#Syntax of an if statement .
# if some_condition:
     # execute some code
# elif some_other_condition:
#  else:
     # do something else

hungry = True
if hungry:
   print('FEED ME!')
else:
   print('Im not hungry')

#******************************************************************************#
loc = 'Bank'
if loc == 'Auto Shop':
    print('Cars are Cool!')
elif loc =='Bank':
    print('Money is Cool!')
elif loc== 'Store':
    print('Welcome to the store!')
else:
    print('I do not know much.')

#******************************************************************************#
# For Loops in Python
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)
my_list =[1,2,3,4,5,6,7,8,9,10]
for jelly in my_list:
    print('hello')
    print(jelly)


for num in my_list:
    # check for even
    if num % 2 ==0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum =0
for num in my_list:
    list_sum = list_sum + num
    print(list_sum)

for i in 'hello world':
    print(i)

for _ in 'hello world':
    print('Coll!')

tup = (1,2,3)
for item in tup:
    print(item)

myList = [(1,2),(3,4),(5,6),(7,8)]
print(f'length={len(myList)}')
for item in myList:
    print(item)
# tupel unbacking
#for (a,b) in myList:
for a,b in myList:
    print(a)
    print(b)
print('***********************************************')
myList = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in myList:
    print(b)

d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)

for item in d.items():
    print(item)

for key,value in d.items():
    print(value)

for value in d.values():
    print(value)

print('#*************************************************#')
# while loop Syntax

# while some_boolean_condition:
    # do somthing
# else:
    # do somthing different

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x+=1
else:
    print("X is not less than 5")
# we can use break & continue & pass

# break : Break out the current enclosing loop.
# continue : Goes to the top of the closest enclosing loop.
# pass : Dose nothing at all .


x = [1,2,3]
for item in x:
    #comment
    pass
print('end of my script')

print('#*************************************************#')

myString = 'Sammy'
for letter in myString:
    if letter == 'a':
       continue
    print(letter)

print('#*************************************************#')

myString = 'Sammy'
for letter in myString:
    if letter == 'a':
       break
    print(letter)

print('#*************************************************#')

x = 0
while x < 5:
    if x == 2:
       break
    print(f'The current value of x is {x}')
    x+=1
else:# this line will not work
    print("X is not less than 5")

print('#********************# Useful operators in Python *****************************#')


for num in range(10):
    print(num)

print('#*************************************************#')

for num in range(3,10):
    print(num)

print('#*************************************************#')

for num in range(0,11,2):# add steps
    print(num)

print('#*************************************************#')
mylist=list(range(0,11,2))
print(mylist)

print('#*************************************************#')

index_count =0
for letter in 'adbc':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

print('#*************************************************#')

word = 'abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)

print('#******************ZIP Operator*******************************#')

myList1 = [1,2,3,4,5,6]
myList2 = ['a','b','c']
myList3 = [100,200,300]
for item in zip (myList1,myList2,myList3):
   print(item)
for a,b,c in zip (myList1,myList2,myList3):
   print(b)
print('#********************IN operator*****************************#')

print('x' in [1,2,3])
print('x' in ['x','y','z'])
print('a' in 'a world')
print('mykey' in {'mykey' :345} )

d = {'mykey' :345}
print(345 in d.keys())
print(345 in d.values())

print('#******************** Min & Max ****************************#')
myList = [1,2,3,4,5,6]
print(f'minimum value is {min(myList)}')
print(f'maximum value is {max(myList)}')

print('#******************** import ****************************#')
from random import shuffle
myList = [1,2,3,4,5,6,7,8,9,10]
shuffle(myList)
print(myList)

from random import randint
print(randint(0,100))
print(randint(0,100))

print('#******************** Enter a number  ****************************#')
res = int(input('Enter a number here : '))

result = input('what is your name ? ')

print(f'hellow {result}')

print('#********************* List Comprehensions ****************************#')

mystring = 'hellow world'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

mylist = [letter for letter in mystring]
print(mylist)

mylist = [letter for letter in 'mystring']
print(mylist)

mylist = [x for x in range(0,11)]
print(mylist)

mylist = [x**2 for x in range(0,11)]
print(mylist)

mylist = [x for x in range(0,11) if x%2==0]
print(mylist)

celcius = [0,10,20,34.4]
fahrenheit = [((9/5)*temp +32 )for temp in celcius]
print(fahrenheit)


fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp +32 ))
print(fahrenheit)

mylist = [x if x%2==0 else 'ODD' for x in range(0,11) ]
print(mylist)

mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)

mylist = [x*y for x in [2,4,6] for y in [100,200,300]]
print(mylist)

print('#********************* Method and Functions ****************************#')
mylist = [1,2,3]
#print(help(mylist.insert))

# def name_of_function(): # Snake casing is all lowercases with underscores between words.

def add_function(num1,num2):
    return num1+num2
result = add_function(4,5)
print(result)

def say_hello(name='Default'):
     print(f'hello {name}')

say_hello('Aliiii')
say_hello()

def even_check(number):
    result = number % 2 == 0
    return result
print(even_check(20))
print(even_check(21))

#  RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST
def check_even_list(list_num):
    for num in list_num:
        if num % 2 == 0:
            return True
        else:
             pass
    return False
result = check_even_list([1,3,5])
print(result)

result = check_even_list([2,4,5])
print(result)

result = check_even_list([1,1,1,1,1,1,1,1,1,4])
print(result)


# RETURN ALL EVEN NUMBERS IN A LIST
def check_even_list(list_num):
    even_list =[]
    for num in list_num:
        if num % 2 == 0:
            even_list.append(num)
        else:
            pass
    return even_list

result = check_even_list([2,4,5])
print(result)
result = check_even_list([1,1,1,1,1,1,1,1,1,4])
print(result)

# TUPLE UNPACKING WITH PYTHON Functions
stock_prices = [('apple',200),('google',800),('msft',500)]
for item in stock_prices:
    print(item)

stock_prices = [('apple',200),('google',800),('msft',500)]
for ticker,price in stock_prices:
    print(ticker)

stock_prices = [('apple',200),('google',800),('msft',500)]
for ticker,price in stock_prices:
    print(price+(0.1*price))

# CHECK EMPLOYEE OF THIS MONTH
def check_employee(employee_list):
    current_max=0
    employee_of_month=''
    for employee,hours in employee_list:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month,current_max)


employee_list = [('Ali',3000),('Samir',4000),('Mizo',2000)]
result = check_employee(employee_list)
print(result)

employee_list = [('Ali',3000),('Samir',4000),('Mizo',2000)]
name,hours = check_employee(employee_list)
print(f'the employee of month {name}')

#*****************interation between python functions *************************/

from random import shuffle

def shuffle_list(myList):
    shuffle(myList)
    return myList

mylist=[1,2,3,4,5,6,7]
shuffle_list(mylist)
print(mylist)

#*****************   *args and **kwargs *************************/
def myfunc(*args):
    for item in args:
        print(item)

myfunc(10,20,30,40,50,60,70)


def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple',veggie='lettuce')


def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,40,fruit='orange',food='eggs',animal='dog')

print(range(len('dsnigfsgknfdksvnfkdsnvf')))

def myfunc(string):
    new_string = ''
    for x in range(len(string)):
        if (x+1)%2==0:
            new_string += string[x].upper()
        else:
            new_string += string[x].lower()
    return new_string

#/************************** Lambda expression and Map **************************************/

def square(num):
    return num**2
my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print('item is {}'.format(item))

print(list(map(square,my_nums)))

#/************************** map
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]

names = ['Andy','Eve','Sally']

print(list(map(splicer,names)))

#/************************** filter

def check_even(num):
    return num%2 == 0
mynums =[1,2,3,4,5,6]
mylist= []
for item in filter(check_even,mynums):
    mylist.append(item)
print(mylist)
#/************************** lambda
square = lambda num: num ** 2
print(square(2))

#print(list(map(square,my_nums)))
print(list(map(lambda num: num ** 2,my_nums)))
print(list(filter(lambda num:num%2==0,mynums)))
print(list(map(lambda x:x[0],names)))
print(list(map(lambda x:x[::-1],names)))

#/************************** LEGB Rule :
#L:Local E:Enclosing G:Global B:Built-in

name ='THIS IS A GLOBAL STRING' #G:Global
def greet():
    name='Sammy' #L:Local

    def hello():
        name ='Ali' #E:Enclosing
        print('Hello '+name)

    hello()

greet()

#/**************************


#***************** Method and Functions *************************/

def up_low(s):
    d = {'lower':0,'upper':0} # dictionary
    for char in s:
        if char.isupper():
            d['upper']+=1
        elif char.islower():
            d['lower']+=1
        else:
            pass
    print(f"Original Strring: {s}")
    print(f'Lowercase count : {d["lower"]}')
    print(f'Uppercase count : {d["upper"]}')


up_low('Hello Mr.Rogers , how are you htis fine Tuesday')

def unique_list(lst):
    return list(set(lst))

list = unique_list([1,1,1,1,1,1,1,2,3,4])
print(list)

def unique_list(lst):
    seen_number = []
    for num in lst:
        if num not in seen_number:
            seen_number.append(num)
    return seen_number

list = unique_list([1,1,1,1,1,1,1,2,3,4])
print(list)



#***************** Object Oriented Programming *************************/
# class NameOfClass():
#       def _init_(self,param1,param2):
#           self.param1 = param1
#           self.param2 = param2

#       def some_method(self):
#           # perform some action
#           print(self.param1)
