import sys

input = sys.stdin.readline

t, d, m = map(int, input().split())
y = [0]
for i in range(m):
    y.append(int(input()))

y.append(d)
f = False
for i in range(1, len(y)):
    if y[i] - y[i-1] >= t:
        f = True
        break

print("Y" if f else "N")
