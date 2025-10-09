s = input()
m = -1
for r in range(1, 101):
    for c in range(1, 101):
        if r * c == len(s) and r <= c:
            m = max(m, r)

for i in range(m):
    for j in range(i, len(s), m):
        print(s[j], end="")
