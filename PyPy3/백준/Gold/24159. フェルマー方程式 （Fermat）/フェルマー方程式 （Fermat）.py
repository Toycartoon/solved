p = int(input())
n = int(input())

z = [0 for _ in range(p)]
pw = [0 for _ in range(p)]
for i in range(p):
    z[pow(i, n, p)] += 1
    pw[i] = pow(i, n, p)

ans = 0
for x in range(p):
    for y in range(p):
        ans += z[(pw[x]+pw[y]) % p]

print(ans)
