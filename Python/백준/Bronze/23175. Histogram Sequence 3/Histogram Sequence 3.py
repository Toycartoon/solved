n = int(input())
a = list(map(int, input().split()))

idx = 0
while idx < n:
    print(a[idx], end=" ")
    idx += a[idx]
