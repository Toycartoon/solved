a = []
for i in range(int(input())):
    s = input()
    n = int(input())
    a.append((n, s))
a.sort(key=lambda x: -x[0])
print(a[0][1])
