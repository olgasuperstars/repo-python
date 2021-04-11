# 1 способ

def my_func(x, y):
    x = float(input('Введите действительное положительное число: '))
    y = float(input('Введите целое отрицательное число: '))

    degree = x ** y
    return (print(degree))
x = 0
y = 0

my_func (x, y)

# 2 способ

x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
z=1
for i in range(abs(y)):
    z/=x
print(z)