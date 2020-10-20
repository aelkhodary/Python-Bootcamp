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
