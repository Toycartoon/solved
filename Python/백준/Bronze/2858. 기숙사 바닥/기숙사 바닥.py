r, b = map(int, input().split())
a = r + b

for i in range(3, a):
    if a % i != 0:
        continue

    l, w = a // i, i
    if (l-2) * (w-2) == b:
        print(l, w)
        break
