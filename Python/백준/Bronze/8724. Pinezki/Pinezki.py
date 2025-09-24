n = int(input())
a = list(map(int, input().split()))
v = []
x = 0
for i in range(n):
    if a[i] == 1:
        x += 1
    else:
        v.append(x)
        x = 0
v.append(x)
print(max(v))
