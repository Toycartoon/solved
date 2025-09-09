f = list(map(int, input().split()))
a, b = input().split()

_a, _b = "", ""
for i in a:
    _a += str(f.index(int(i)))

for i in b:
    _b += str(f.index(int(i)))

ab = int(_a) + int(_b)
for i in str(ab):
    print(f[int(i)], end="")
