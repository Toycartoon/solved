n = int(input())
a = [0]
s = set()

s.add(0)
for i in range(1, n+1):
    v = a[-1] - i
    if v < 0 or v in s:
        v = a[-1] + i
    a.append(v)
    s.add(v)
print(a[-1])
