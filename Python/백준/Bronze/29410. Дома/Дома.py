n, a, b = map(int, input().split())

ans = 0
for _ in range(n):
    c = list(map(int, input().split()))
    for i in c[1:]:
        s = bin(i)[2:]
        ans += s.count("0") * a
        ans += s.count("1") * b
print(ans)
