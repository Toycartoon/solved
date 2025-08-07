n = int(input())
g = [[*input()] for _ in range(n)]

f = True
for i in g:
    if i.count("B") != i.count("W") or i.count("BBB") >= 1 or i.count("WWW") >= 1:
        f = False
        break

for i in zip(*g):
    i = "".join(i)
    if i.count("B") != i.count("W") or i.count("BBB") >= 1 or i.count("WWW") >= 1:
        f = False
        break

print(int(f))
