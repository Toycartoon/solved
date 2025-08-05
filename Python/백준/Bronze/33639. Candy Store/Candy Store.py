n, q = map(int, input().split())
w = {}
for i in range(n):
    f, l = input().split()
    if f[0] + l[0] in w:
        w[f[0]+l[0]] = "ambiguous"
    else:
        w[f[0]+l[0]] = f"{f} {l}"

for i in range(q):
    s = input()
    if s in w:
        print(w[s])
    else:
        print("nobody")
