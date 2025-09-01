n = int(input())
a = list(map(int, input().split()))

f = True
for i in range(n):
    if i % 2 == a[i] % 2:
        f = False
        break

if f:
    print("YES")
else:
    print("NO")
