n, m = map(int, input().split())

f = 0
g = 1
for i in range(m+1):
    if i % 2 == 0:
        if n < i+1:
            print(f, end="")
        f += g
        f %= 10
    else:
        if n < i+1:
            print(g, end="")
        g += f
        g %= 10
