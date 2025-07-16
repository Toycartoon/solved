from itertools import permutations as perm

a, b, c = map(int, input().split())
ans = 0
for _a, _b, _c in perm((a, b, c), 3):
    ans = max(ans, _a + _b * _c)

print(ans)
