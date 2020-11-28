#***************** Object Oriented Programming *************************/
# class NameOfClass():
#       def __init__(self,param1,param2): # self-->connect this method to the instance of the class
#           self.param1 = param1
#           self.param2 = param2

#       def some_method(self):
#           # perform some action
#           print(self.param1)


class Sample():
      pass
my_sample = Sample()
print(type(my_sample))

class Dog():
    def __init__(self,breed):
        # Attributes
        # we take in the argument
        # assign it using self.attribute_name
        self.breed = breed

my_dog = Dog(breed='Lab')
print(my_dog.breed)


class Dog():
    def __init__(self,my_breed):
        # Attributes
        # we take in the argument
        # assign it using self.attribute_name
        self.my_attribute = my_breed

my_dog = Dog(my_breed='Huskie')
print(my_dog.my_attribute)


class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        # Expect boolean True/False
        self.spots = spots

    # OPERATIONS/ACTIONS--->METHODS
    def bark(self):# self-->connect this method to the instance of the class
        print('WOOF! My name is {}'.format(self.name))


my_dog = Dog(breed='Huskie',name='Sammy',spots=False)
print(my_dog.species)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.bark())
#***************** CLASS OBJECT ATTRIBUTE *************************/
class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        # Expect boolean True/False
        self.spots = spots

    # OPERATIONS/ACTIONS--->METHODS
    def bark(self,number):# self-->connect this method to the instance of the class
        print('WOOF! My name is {} and the number is {}'.format(self.name ,number))


my_dog = Dog(breed='Huskie',name='Sammy',spots=False)
print(my_dog.species)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.bark(10))


class Circle():
    #CLASS OBJECT ATTRIBUTE
    pi = 3.14
    def __init__(self,radius=1):

       self.radius = radius
       self.area = radius * radius * Circle.pi
    #Method
    def get_circle_reference(self):
        return self.area

my_circle = Circle(30)
print(my_circle.radius)
print(my_circle.get_circle_reference())

#*********** Object Oriented Programming- Inheritance and polymorphism *************/
class Animal():
    def __init__(self):
        print("Animal Creayed")

    def who_am_i(self):
        print("I am an animal ")

    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')
    # Override method
    def who_am_i(self):
        print("I am dog ")

    def bark(self):
        print('Huskie')

mydog = Dog()
# Override
mydog.who_am_i()
# original
mydog.eat()
# New
mydog.bark()

#*********** Object Oriented Programming- Polymorphism *************/

# two usage
# 1- two classes have smae function
# 2- when we have abstract class

# 1- two classes have smae function
class Dog():
    def __init__(self,name):
        self.name = name
    def speack(self):
        return "my name is " + self.name

class Cat():
    def __init__(self,name):
        self.name = name
    def speack(self):
        return "my name is " + self.name

dog = Dog("haski")
cat = Cat("Lyly")
for pet in [dog,cat]:
    print(pet.speack())

# 2- when we have abstract class

class Animal():
    def __init__(self,name):
        self.name = name

    def speack(self):
        raise NotImplementedError("should implemnted by sup class ")

# animal = Animal("haski")
# animal.speack()

class Dog(Animal):
    def speack(self):
        return "my name is " + self.name

class Cat(Animal):
    def speack(self):
        return "my name is " + self.name

dog = Dog("haski")
cat = Cat("Lyly")

def animal(inst):
     print(inst.speack())
animal(dog)
animal(cat)

#*********** Object Oriented Programming  Special(Magic/Dunder) Methods *************/

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self): # what happend when we delete instance from class
        print('A Book object has been deleted')

b = Book('Python rocks','Jose',200)
print(b)
print(str(b))
print(len(b))
del b
#del(b)

#*********** Challenge Solution *************/
class Account():

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):
        self.balance += dep_amt
        print(f"Added {dep_amt} to the balance")

    def withdrawal(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('withdrawal accepted')
        else:
            print('Sorry No balance in your account')

    def __str__(self):
       return f"Owner : {self.owner} \nBalance: {self.balance}"

a = Account('Sam' , 500)
print(a)
a.deposit(300)
print(a)
a.withdrawal(800)
print(a)

#*********** Modules and Packages *************/
# PyPI is a repository for open source third-party Python packages.
# It's similar to NPM for Node.js
# We can use 'pip install' at the command line to install these packages.
# By installing Python from python.org or through the Anaconda distribution
# you also installed pip
# pip is a simple way to download packages at your command line directly from the
# PyPi repository
# > pip install <pakage-name>
# > pip install requests
# > pip install colorama
# > pip install openpyxl
# > import openpyxl
# > quit()
#*********** Writing your own modules and packages *************/

# modules are just.py scripts that you call in another.py script .
# packages are collection of modules .
