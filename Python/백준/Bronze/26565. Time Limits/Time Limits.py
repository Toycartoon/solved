from math import ceil

for _ in range(int(input())):
    n, s = map(int, input().split())
    t = list(map(int, input().split()))

    t.sort(reverse=True)
    print(ceil((t[0] * s) / 1000))
