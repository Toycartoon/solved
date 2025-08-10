n = int(input())
a = [0 for _ in range(26)]

for i in range(n):
    s = input()
    a[ord(s[0])-65] += 1

ans = 0
for i in a:
    if i >= 1:
        ans += 1
    else:
        break

print(ans)
