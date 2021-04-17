def data_user(name, surname, year_of_birth, city, email, cell):
    name = input('Введите Ваше имя: ')
    surname = input('Введите Вашу фамилию: ')
    year_of_birth = input('Введите Ваш год рождения: ')
    city = input('Введите Ваш город проживания: ')
    email = input('Введите адрес элетронной почты: ')
    cell = input('Введите контактный номер телефона: ')
    return(print(f'{name} {surname}, {year_of_birth}, {city}, {email}, {cell}'))
a=0
b=0
c=0
d=0
e=0
f=0
person = data_user(a,b,c,d,e,f)
