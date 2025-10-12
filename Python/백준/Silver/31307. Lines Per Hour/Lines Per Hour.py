n, lph = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()

ans = 0
lph *= 5
for i in a:
    if lph-i >= 0:
        ans += 1
        lph -= i
    else:
        break
print(ans)
