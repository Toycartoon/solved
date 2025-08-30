ans = 100
m = 100
for c in range(int(input())):
    v = int(input())
    m += v
    ans = max(m, ans)

print(ans)
