n = int(input())
for i in range(n):
    if i % 2 == 0:
        print(*range(i*n+1, (i+1)*n+1))
    else:
        print(*range((i+1) * n, i*n, -1))
