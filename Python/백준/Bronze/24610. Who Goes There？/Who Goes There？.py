n, m = map(int, input().split())
t = []
for i in range(m):
    t.append(int(input()))

a = [0 for _ in range(m)]
idx = 0
while n > 0 and a != t:
    if a[idx] < t[idx]:
        a[idx] += 1
        n -= 1
    idx = (idx + 1) % m

for i in a:
    print(i)
