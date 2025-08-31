a = list(map(int, input().split()))
while a != [*range(1, 6)]:
    for i in range(4):
        if a[i] > a[i+1]:
            a[i+1], a[i] = a[i], a[i+1]
            print(*a)
