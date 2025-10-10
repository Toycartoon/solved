from math import trunc

for t in range(int(input())):
    n, *a = map(int, input().split())
    s = sum(a) / n

    v = 0
    for i in a:
        if i > s:
            v += 1
    print(f"{trunc(s * 1000 + 0.5) / 1000:.03f} {trunc((v / n) * 100000 + 0.5) / 1000:.03f}%")
