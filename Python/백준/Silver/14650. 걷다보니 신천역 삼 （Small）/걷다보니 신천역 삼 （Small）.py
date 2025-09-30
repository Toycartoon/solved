from itertools import product as prod

n = int(input())
ans = 0
for i in prod(["0", "1", "2"], repeat=n):
    s = "".join(i)
    if s[0] != "0" and int(s) % 3 == 0:
        ans += 1
print(ans)
