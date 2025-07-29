n = int(input())
ans = 0
a = input()
b = input()

for i in range(n):
    mx = max(ord(a[i]), ord(b[i]))
    mn = min(ord(a[i]), ord(b[i]))
    ans += min(mx-mn, 90-mx + mn-64)

print(ans)
