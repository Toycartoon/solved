from math import trunc

for t in range(int(input())):
    c, b, n, r = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        a, p = map(int, input().split())
        if a in x:
            ans += trunc(p * (r / 100))
    print(f"Data Set {t+1}:")
    print(ans)
    print()
