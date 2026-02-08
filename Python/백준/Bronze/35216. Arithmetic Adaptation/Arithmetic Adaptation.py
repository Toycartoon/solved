n = int(input())
if n == 0:
    print(-1, 1)
elif n == 1:
    print(-1, 2)
elif n == -999:
    print(-998, -1)
else:
    print(1, n-1)