n = int(input())
a = []
for i in range(1, n+1):
    v = [n, i]
    while v[-1] >= 0:
        v.append(v[-2] - v[-1])

    v.pop()
    if len(a) < len(v):
        a = v

print(len(a))
print(*a)
