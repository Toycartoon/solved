w = {}
x = []
for _ in range(int(input())):
    s = input()
    x.append(s)
    for i in range(len(s)):
        if s[i] in w:
            w[s[i]] += 36 ** (len(s) - (1 + i))
        else:
            w[s[i]] = 36 ** (len(s) - (1 + i))

for i in w.keys():
    w[i] *= (35 - int(i, 36))

k = int(input())
v = sorted(w.items(), key=lambda x: (x[0] == "Z", -x[1], x[0]))
c = set()
for i in range(min(k, len(v))):
    c.add(v[i][0])

a = 0
for i in x:
    for j in c:
        i = i.replace(j, "Z")
    a += int(i, 36)

ans = ""
while a >= 36:
    m = a % 36
    a //= 36

    if m < 10:
        ans += str(m)
    else:
        ans += chr(m + 55)

m = a % 36
if m < 10:
    ans += str(m)
else:
    ans += chr(m + 55)

print(ans[::-1])
