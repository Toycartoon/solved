from itertools import permutations as perm

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in perm(a, n):
    v = 0
    for x in range(1, n):
        v += abs(i[x-1] - i[x])
    ans = max(ans, v)
print(ans)
