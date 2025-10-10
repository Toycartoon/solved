n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        v = [*a]
        v[i], v[j] = v[j], v[i]
        f = True
        for x in range(n):
            if v[x] % 2 == x % 2:
                f = False
                break
        if f:
            print(i+1, j+1)
            exit()
print(-1, -1)
