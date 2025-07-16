a, b = input().split()
a = a.zfill(max(len(a), len(b)))
b = b.zfill(len(a))

for i in range(len(a)):
    print(int(a[i]) + int(b[i]), end="")
