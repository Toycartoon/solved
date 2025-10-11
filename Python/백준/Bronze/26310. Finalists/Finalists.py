n = int(input())
a = []
for i in range(6):
    s, pt, pu, rt, ru, f = input().split()
    a.append((s, (0.56 * int(ru) + 0.24 * int(rt) + 0.14 * int(pu) + 0.06 * int(pt) + 0.3 * int(f))))
a.sort(key=lambda x: -x[1])

ans = 0
for i in range(n):
    if a[0][0] == "Taiwan":
        ans += 1
    a = a[1:] + [a[0]]
print(ans)
