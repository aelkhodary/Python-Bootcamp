#one.py
def func():
    print("Func() IN ONE.PY")

print('TOP LEVEL IN ONE.PY')

if __name__ == '__main__':
    print('ONE.PY is being run directory !')
else:
    print('ONE.PY has been imported!')