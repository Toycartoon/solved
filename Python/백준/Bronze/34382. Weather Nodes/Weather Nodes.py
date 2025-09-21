n = int(input())
if n == 0:
    print(0)
    exit()
a = []
for i in range(n):
    a.append(float(input()))

s = sum(a) / n
ans = 0
for i in a:
    if abs(i - s) > 10:
        ans += 1
print(ans)
