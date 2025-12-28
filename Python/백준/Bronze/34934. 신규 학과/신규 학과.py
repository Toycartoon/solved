a = []
for _ in range(int(input())):
    s, v = input().split()
    a.append((s, int(v)))
a.sort(key=lambda x: -x[1])
print(a[0][0])
