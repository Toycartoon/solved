n, s = input().split()
a = []
ans = ""
for i in range(int(n)):
    name, txt = input().split()
    if name == s:
        ans = txt
        break
    a.append((name, txt))

v = set()
for x, t in a:
    if t == ans:
        v.add(x)
print(len(v))
