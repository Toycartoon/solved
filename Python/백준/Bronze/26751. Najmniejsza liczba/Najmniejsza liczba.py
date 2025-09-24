from itertools import permutations as perm

ans = 1000
a = input().split()
for i in perm(a, 3):
    if i[0] != "0":
        ans = min(ans, int("".join(i)))
print(ans)
