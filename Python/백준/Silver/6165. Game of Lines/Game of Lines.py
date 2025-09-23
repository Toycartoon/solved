from fractions import Fraction as f

n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

s = set()
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[j][0] - a[i][0] == 0:
            s.add(float('inf'))
        else:
            s.add(f(a[j][1]-a[i][1], a[j][0]-a[i][0]))
print(len(s))
