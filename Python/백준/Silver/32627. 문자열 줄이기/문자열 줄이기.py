n, m = map(int, input().split())
s = input()

a = [0 for _ in range(26)]
for i in s:
    a[ord(i)-97] += 1

for i in range(26):
    if a[i] <= m:
        m -= a[i]
        a[i] = 0
    else:
        a[i] -= m
        break

ans = []
for i in s[::-1]:
    if a[ord(i)-97] > 0:
        ans.append(i)
        a[ord(i)-97] -= 1

print(*ans[::-1], sep="")
