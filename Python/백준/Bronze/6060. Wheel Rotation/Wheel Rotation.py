n = int(input())
w = {}
for i in range(n-1):
    s, d, c = map(int, input().split())
    w[s] = (d, c)

c = False
ptr = 1
while ptr != n:
    f, r = w[ptr]
    if r == 1:
        c = not c
    ptr = f
print(int(c))
