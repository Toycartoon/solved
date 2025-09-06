n, m = map(int, input().split())
a = []
s = [0 for _ in range(n)]
for i in range(n):
    a.append(list(sorted(map(int, input().split()), reverse=True)))

for g in zip(*a):
    mx = max(g)
    for i in range(n):
        if g[i] == mx:
            s[i] += 1

mx = max(s)
for i in range(n):
    if s[i] == mx:
        print(i+1, end=" ")
