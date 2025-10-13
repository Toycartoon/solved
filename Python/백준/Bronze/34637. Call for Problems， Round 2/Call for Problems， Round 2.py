n, k = map(int, input().split())
d = []
for i in range(n):
    d.append(int(input()))

s = set()
idx = 0
while idx < n and len(s) < k:
    s.add(d[idx])
    idx += 1
print(len(s))
