n = int(input())
g = [[*input()] for _ in range(n)]

mx = max(zip(*g), key=lambda i: i.count("Y")).count("Y")
ans = []
for i in range(5):
    if list(zip(*g))[i].count("Y") == mx:
        ans.append(i+1)

print(*ans, sep=",")
