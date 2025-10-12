n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

b = []
for i in range(n):
    b.append(int(input()))

a.sort()
b.sort()
ans = 0
for i in range(n):
    ans += abs(a[i]-b[i])
print(ans)
