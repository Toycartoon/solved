n = int(input())
w = int(input())
s = n * 10
if n >= 3:
    s += 20
if n == 5:
    s += 50

if w > 1000:
    s = max(s-15, 0)

print(s)
