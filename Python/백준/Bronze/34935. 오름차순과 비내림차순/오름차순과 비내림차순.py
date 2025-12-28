n = int(input())
a = list(map(int, input().split()))
f = True
for i in range(1, n):
    if a[i-1] == a[i]:
        f = False
        break
print(int(f))
