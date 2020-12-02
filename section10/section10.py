#***************** Errors and Exceptions *************************/
def add():
    try:
        # May have an error
        res = 10 + 10
        print(res)

    except:
        print("\nHey it looks like you aren't adding correctly!\n")

    else:
        print("\nAdd went well!")
        print(res)

    finally:
        print("I always run")

def open_file():

    try:
        f = open('file.txt','w')
        f.write('Write test line')
        print("file update successfully")

    except TypeError:
        print("There was type error")

    except OSError:
        print('Hey you have an OS Error')

    except:
        print('catch all error here')

    finally:
        print('I will always run at the end')
        f.close()

def ask_for_int():

    while True:
        try:
            res = int(input("Please provide number :"))
        except:
            print("Whoops! That is not anumber")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print('End of try/except/finally')
            print('I will always run at the end')







#***************** Python testing tools *************************/
'''
 There are several testing tools ,we will focus on two
 pylint : This is a library that looks at your code and reports back possible issues
 unittest : This built-in library will allow to test your own programs and check you
  are getting desired outputs.
'''

#> pip install pylint
def unit_test():
    #> pip install pylint
    #> pylint section10.py
    a =10
    b =10
    res = a+B



if __name__ == '__main__':
    print('--------------run directory!-----------')
    #add()
    #open_file()
    #ask_for_int()
    unit_test()
else:
    print('ONE.PY has been imported!')
