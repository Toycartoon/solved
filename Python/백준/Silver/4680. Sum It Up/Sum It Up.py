from itertools import combinations as comb

while True:
    n, m, *x = map(int, input().split())
    if n == m == 0:
        break

    print(f"Sums of {n}:")
    s = set()
    for i in range(1, m+1):
        for v in comb(x, i):
            if sum(v) == n:
                s.add(v)

    if len(s) == 0:
        print("NONE")
    else:
        for i in sorted(list(s), reverse=True):
            print(*i, sep="+")
