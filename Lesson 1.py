# Task 1

name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))

print(f'Вас зовут {name}, Вам {age} лет(года)')

# Task 2

second = int(input('Введите количество секунд: '))
minute = second // 60
second_fin = second % 60
hour_fin = minute // 60
minute_fin = minute % 60

print(f'{hour_fin}:{minute_fin}:{second_fin}')

# Task 3

a = input('Введите целое положительное число: ')
aa = (a + a)
aaa = (a + a + a)
b = int(int(a) + int(aa) + int(aaa))

print(b)

# Task 4

a = int(input('Введите целое полжительное число: '))
b = 0
while a != 0:
    if a % 10 > b:
        b = a % 10
    a = a // 10

print(b)

# Task 5

income = float(input('Введите выручку компании: '))
cost = float(input('Введите издержки компании: '))
profit = float(income - cost)
if profit > 0:
    print('У Вас прибыльный бизнес')
else:
    print('Вы работаете в убыток')

count = int(input('Введите количество сотрудников в Вашей компании: '))

if profit > 0:
    profit_person = float(profit / count)
    print(f'Прибыль в расчете на одного сотрудника = {profit_person}')

# Task 6

a = float(input('Введите количество км, которые спортсем пробежал в 1-й день: '))
b = int(input('Введите минимальное количестов км, которое должен пробежать спортсмет: '))
day = 1

while a <= b:
    a = a * 1.1
    day += 1

print(f'На {day}-й день спортсмен пробежал не менее {b} км')
