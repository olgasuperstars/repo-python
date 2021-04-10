a = []

for i in range(5):
    a.append(input('Введите число или текст: '))

print(a)

a.insert(0,a[1])
a.pop(2)

print(a)

a.insert(2,a[3])
a.pop(4)

print(a)