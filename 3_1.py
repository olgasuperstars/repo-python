a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

def div(a, b):
    result = a / b
    return(result)

if b != 0:
    result = div(a, b)
    print(result)
else:
    print('на ноль дельить нельзя')
