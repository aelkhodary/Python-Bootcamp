'''
* Generator functions allow us to write a function that can send back a value
  and then later resume to pick up where it left off.

* It allowing us to generate a sequence of values over time

* The main difference in syntax will be the use of 'yield' statement

* When a generator function is compiled they become an object that supports an
  iteration protocol.
* That means when they are called in your code they don't actually return a value
   then exit

* Let's explore how to create our own generators!


'''

def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))
for x in create_cubes(10):
    print(x)

'''
/************************************************/
'''
print('\n************************************************\n')

def create_cubes(n):
    for x in range(n):
        yield x**3


print(create_cubes(10))
for x in create_cubes(10):
    print(x)

'''
/************************************************/
note: yield is agood function in case of you want to iterate
'''
print('\n************************************************\n')

def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for x in gen_fibon(10):
    print(x)


'''
/************************************************/
use 'next'
'''
print('\n************************************************\n')

def simple_gen():
    for x in range(3):
        yield x

for x in simple_gen():
    print(x)

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))
#print(next(g))   
