def my_func(x, y):
    z = 1
    print(x, y, z)
my_func(2, 5)
my_func(y = 2, x = 5)

# arbitrary args, *args
def my_func(*x):
    z = len(x)
    print("there are ", z, "arguments")
my_func(2, 5, 7, 9)

# arbitrary kwargs, **kwargs
def my_func(**x):
    print(x)
    z= (x.keys())
    print(z)
    a = 1
    for i in x.values():
        print(i)
        a *= i
    return a

result = my_func(x = 3, t = 5, g = 6)
print(result)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# recursion
def factorial(x):
    if x > 1:
        return x * factorial(x-1)
    else:
        return 1

x = factorial (4)
print("factorial is: ", x)

x = lambda a, b : a + b
print(x(1, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

triple = myfunc(3)
print(triple(11))