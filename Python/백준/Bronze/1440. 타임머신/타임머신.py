from itertools import permutations as perm

a, b, c = map(int, input().split(":"))
ans = 0
for i, j, k in perm(("1 <= x <= 12", "0 <= x <= 59", "0 <= x <= 59"), 3):
    if eval(i.replace("x", str(a))) and eval(j.replace("x", str(b))) and eval(k.replace("x", str(c))):
        ans += 1

print(ans)
