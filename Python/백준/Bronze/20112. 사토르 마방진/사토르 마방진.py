n = int(input())
s = [[*input()] for _ in range(n)]

x = []
for y in range(n):
    x.append("".join(s[y]))

f = True
for i in range(n):
    if "".join(list(zip(*s))[i]) != x[i]:
        f = False
        break

if f:
    print("YES")
else:
    print("NO")
