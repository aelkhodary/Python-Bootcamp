
'''
Decorators
Now you want to add some new capabilities to the function

def simple_func():
    # Want to do more stuff!
    # Do simple stuff
    return somthing

You now have two option:
  * Add that extra code (functionality) to your old function
  * Create a brand new function that contains the old code , and then add
  new code to that.

Python has decorators that allow you to tack on extra functionality to an
already existing function.
They use the @ operator and are then placed on top of the original function

@some_decorator
def simple_func():
    # Do simple stuff
    return something

'''

def hello(name='Jose'):
    print('The Hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is the welcome() func inside hello!'

    print(greet())
    print(welcome())
    print('This is the end of the hello function')





#hello()

'''
/************************************************/
'''

'''
Return a function inside an function
'''

def hello(name='Jose'):
    print('The Hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is the welcome() func inside hello!'

    print('I am going to return a function!!')

    if name == 'Jose':
        return greet
    else:
        return welcome

my_new_func = hello('Jose')
print(my_new_func)
print(my_new_func())

'''
/************************************************/
'''

'''
Pass a function inside an function and execut it
'''

def hello():
    return 'Hi Jose!'

def other(some_def_func):
    print('other code runs here')
    print(some_def_func())


other(hello)

'''
/************************************************/
'''

def new_decorator(original_func):

    def wrap_func():

        print('Some extra code , before the original function')

        original_func()

        print('Some extra code , after the original function')

        print('\n************************************************\n')

    return wrap_func

def func_needs_decorator():
    print('I want to be decorated')

'''
/***********/
'''
#func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)

decorated_func()

'''
/***********/
'''
@new_decorator
def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()
