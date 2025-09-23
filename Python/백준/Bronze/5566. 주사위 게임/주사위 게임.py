n, m = map(int, input().split())
x = []
for i in range(n):
    x.append(int(input()))

s = 0
for i in range(m):
    j = int(input())
    s += j
    if s >= n-1 or (s < n and s + x[s] >= n-1):
        print(i+1)
        break
    s += x[s]
