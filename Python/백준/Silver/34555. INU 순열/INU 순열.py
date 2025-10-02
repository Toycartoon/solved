n = int(input())
a = [n]
pos = False
v = n-1
while v > 0:
    if pos:
        n += v
        a.append(n)
    else:
        n -= v
        a.append(n)
    v -= 1
    pos = not pos
print(*a[::-1])