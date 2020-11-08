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
print('******************************')
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
