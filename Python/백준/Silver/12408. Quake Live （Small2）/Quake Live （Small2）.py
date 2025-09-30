from itertools import combinations as comb

for t in range(int(input())):
    n, *a = map(int, input().split())
    s = sum(a)

    ans = float('inf')
    for v in comb(a, n//2):
        i = sum(v)
        ans = min(ans, abs(s-2*i))
    print(f"Case #{t+1}: {ans}")
