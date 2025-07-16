n, r = map(int, input().split())
o1, o2 = 0, 0

for i in range(n):
    p = int(input())

    if p * 2 > r * 2:
        o2 += 1
    elif p * 2 < r * 2:
        o1 += 1

if o1 > o2:
    print(1)
elif o1 < o2:
    print(2)
else:
    print(0)
