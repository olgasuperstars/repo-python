def int_func(a):
    c=''
    a=a.split(' ')
    for i in range(len(a)):
        b=a[i][:1].upper()
        c += b+a[i][1:] + ' '
    return(c)
while True:
    a=input("Введите слова: ")
    print(int_func(a))
    break