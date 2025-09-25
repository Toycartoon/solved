w = {}

for _ in range(int(input())):
    s = input()
    for i in range(len(s)):
        try:
            w[s[i]] += 10 ** (len(s) - (1 + i))
        except KeyError:
            w[s[i]] = 10 ** (len(s) - (1 + i))

v = list(w.values())
v.sort(reverse=True)
for i in range(1, len(v) + 1):
    v[i - 1] = v[i - 1] * (10 - i)

print(sum(v))