n, d, k = map(int, input().split())
a = []
for i in range(n):
    name, w = input().split()
    a.append((int(w), name))
a.sort(reverse=True)

s = 0
for i in range(k):
    s += a[i][0]

if s < d:
    print("impossible")
    exit()
else:
    print(k)
    for i in range(k):
        print(f"{a[i][1]}, YOU ARE FIRED!")
