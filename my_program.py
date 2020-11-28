# from <module> import <function or class>
from my_module import *
# from my_module import my_func
# from my_module import Account

my_func()

a = Account('Sam' , 500)
print(a)
a.deposit(300)
print(a)
a.withdrawal(800)
print(a)

# from <package> import <module>
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import sub_script

some_main_script.report_main()
sub_script.sub_report()

#*********** __name__ and "__main__" *************/
# if __name__ == "__main__":
# Sometimes when you are importing from module , you would like to know
# whether a modules function is being used as an import ,or if you are using
# the original.py file of that module ....
# check file one.py & two.py
# How to use it
def func_1():
    pass
def func_2():
    pass
def func_3():
    pass

if __name__=='__main__':
    # Run the script!
    func_1()
    func_2()
    func_3()
