from itertools import permutations as perm

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in perm(a, n):
    f = True
    w = 500
    for v in i:
        w += v-k
        if w < 500:
            f = False
            break
    if f:
        ans += 1
print(ans)
