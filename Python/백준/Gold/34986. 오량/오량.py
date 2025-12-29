from math import comb

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if set(a) == {1}:
        print(1)
        continue

    ans = 1
    for i in a:
        if i == 0:
            continue

        ans *= comb(n, i)
        n -= i
    print(ans % 1000000007)
