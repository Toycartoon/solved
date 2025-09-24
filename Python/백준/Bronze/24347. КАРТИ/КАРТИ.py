from itertools import permutations as perm

c = input().split()
ans = 0
for i in perm(c, 4):
    ans = max(int("".join(i)), ans)
print(ans)
