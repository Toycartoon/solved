n = int(input())
a = list(map(int, input().split()))
k = int(input())
for i in range(n // k, n+1, n // k):
    print(*sorted(a[i-(n//k):i]), end=" ")
