from functools import reduce
def func (a, b):
    return a * b
c = [i for i in range(100, 1001)  if i % 2 == 0]
print(c)
print(reduce(func, c))