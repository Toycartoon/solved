a = []
k = int(input())
s = input()

v = 1
for i in range(1, k):
    if s[i-1] == s[i]:
        v += 1
    else:
        a.append(v)
        v = 1
a.append(v)

ans = 0
idx = 1
while idx < len(a):
    ans = max(min(a[idx-1], a[idx]) * 2, ans)
    idx += 1
print(ans)
