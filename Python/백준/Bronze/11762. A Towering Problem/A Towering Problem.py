from itertools import permutations as perm

a = list(map(int, input().split()))
u, v = a[-2], a[-1]
for i in perm(a[:-2], 6):
    if sum(i[:3]) == u and sum(i[3:]) == v:
        print(*sorted(i[:3], reverse=True), *sorted(i[3:], reverse=True), sep=" ")
        break
