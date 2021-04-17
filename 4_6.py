from itertools import count, cycle

for i in count(3):
    print(i)
    if i == 10:
        break

count = 0
for i in cycle(['Golden', 'Gate', 'bridge', 'Crimea', 'bridge']):
    count +=1
    print(i)
    if count == 3:
        break
