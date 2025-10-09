n, s = map(int, input().split())
t = s
ans = 0
for i in range(n):
    v = input()
    if v[-1] == "L":
        a = int(v[0]) + 1
    else:
        a = int(v[0])

    if a > t:
        t = s
        ans += 1
    t -= a
print(ans)
