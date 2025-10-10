w = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
n, m = map(int, input().split())
a, b = input().split()

s = []
for i in range(min(n, m)):
    s.append(a[i])
    s.append(b[i])
s.extend([*a[m:]] if n >= m else [*b[n:]])
for v in range(len(s)):
    s[v] = w[ord(s[v])-65]

while len(s) > 2:
    ns = []
    for i in range(1, len(s)):
        ns.append((s[i-1] + s[i]) % 10)
    s = ns
print(f"{s[1]}%" if s[0] == 0 else f"{s[0]}{s[1]}%")
