#two.py
from one import func

func()

def func():
    print("Func() IN TWO.PY")

print('TOP LEVEL IN TWO.PY')

if __name__ == '__main__':
    print('TWO.PY is being run directory !')
else:
    print('TWO.PY has been imported!')
