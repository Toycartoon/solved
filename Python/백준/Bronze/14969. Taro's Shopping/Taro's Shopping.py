from itertools import combinations as comb

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    a = list(map(int, input().split()))
    ans = -1
    for i in comb(a, 2):
        if sum(i) <= m:
            ans = max(ans, sum(i))
    print(ans if ans >= 0 else "NONE")
