def trans(n, b):
    a = ""
    while n >= b:
        m = n % b
        n //= b
        a += str(m)
    m = n % b
    a += str(m)
    return a[::-1]

n, k = map(int, input().split())
v = trans(n, k).split("0")

s = 0
for i in v:
    if len(i) == 0:
        continue
    s += int(i)
print(trans(s, k))
