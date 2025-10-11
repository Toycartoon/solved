n = int(input())
t, d = map(int, input().split())

v = 0
for i in range(n-1):
    dt, dd = map(int, input().split())
    v = max(v, (dd - d) // (dt - t))
    t, d = dt, dd
print(v)
