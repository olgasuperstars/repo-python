b=0
while True:

    a=list(map(str,input('строку чисел, разделенных пробелом, для выхода введите "/": ').split()))

    for i in range(len(a)):
        if a[i]== '/':
            break
        b+=int(a[i])
    if a[i]=='/':
        break
    print(b)

print(b)
