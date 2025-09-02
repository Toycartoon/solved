n, m = map(int, input().split())
g = [[*input()] for _ in range(n)]

w = {".": ".", "O": "O", "-": "|", "|": "-", "/": "\\", "\\": "/", "^": "<", "<": "v", "v": ">", ">": "^"}
z = list(zip(*g))
for y in range(m-1, -1, -1):
    for x in range(n):
        print(w[z[y][x]], end="")
    print()
