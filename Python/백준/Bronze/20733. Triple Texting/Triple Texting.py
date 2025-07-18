from collections import Counter as count

s = input()
i = len(s) // 3

a, b, c = s[:i], s[i:2*i], s[2*i:]
ans = ""
for x in range(i):
    ans += count((a[x], b[x], c[x])).most_common(1)[0][0]

print(ans)
