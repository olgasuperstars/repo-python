a = [2, 67, 77, 3, 1, 12]

new_list = [a[i] for i in range(1, len(a)) if a[i] > a[i-1]]
print(new_list)

