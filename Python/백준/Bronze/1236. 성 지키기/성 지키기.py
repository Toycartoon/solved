n, m = map(int, input().split())
g = [[*input()] for _ in range(n)]

r, c = n, m
for y in g:
    if "X" in y:
        r -= 1

for x in zip(*g):
    if "X" in x:
        c -= 1

print(max(r, c))
