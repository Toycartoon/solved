n, m = map(int, input().split())
x = 1
for i in range(n, 0, -1):
    x *= 2 * i

if x < m:
    print("Nope")
else:
    print("Harshat Mata")
