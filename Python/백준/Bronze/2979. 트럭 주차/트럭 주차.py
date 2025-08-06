a, b, c = map(int, input().split())
t = [0 for _ in range(101)]
for i in range(3):
    s, e = map(int, input().split())
    for v in range(s, e):
        t[v] += 1

print(t.count(1) * a + t.count(2) * 2 * b + t.count(3) * 3 * c)
