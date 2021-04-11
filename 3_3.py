def my_func(x, y, z):
    x = float(input('Введите число: '))
    y = float(input('Введите число: '))
    z = float(input('Введите число: '))
    a = x + y
    b = x + z
    c = y + z
    return(print(max(a, b, c)))

x = 0
y = 0
z = 0
my_func (x, y, z)