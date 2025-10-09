from itertools import permutations as perm

l = list(map(int, input().split()))
for a, b, c, ab, bc, ca, abc in perm(l, 7):
    if a <= b <= c and a + b == ab and b + c == bc and c + a == ca and a + b + c == abc:
        print(a, b, c)
        break
