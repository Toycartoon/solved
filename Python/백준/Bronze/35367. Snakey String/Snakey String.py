r, c = map(int, input().split())
g = [input() for _ in range(r)]
for i in zip(*g):
    print("".join(i).replace(".", ""), end="")
