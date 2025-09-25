a = [[1, 2], [3, 4]]
for i in input():
    if i == "H":
        a[0], a[1] = a[1], a[0]
    elif i == "V":
        a[0] = a[0][::-1]
        a[1] = a[1][::-1]

for i in a:
    print(*i)
