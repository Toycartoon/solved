a = input()
b = input()

c = tuple(map(int, a.split(".")))
d = tuple(map(int, b.split(".")))

if max(float(a), float(b)) == float(a) and c > d:
    print(a)
elif max(float(a), float(b)) == float(b) and d > c:
    print(b)
else:
    print(-1)
