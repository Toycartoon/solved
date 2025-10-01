a, b = 0, 0
w = {}
for i in range(int(input())):
    s = input()
    w[s] = 0

for i in range(int(input())):
    ab, t = input().split()
    x, y = map(int, ab.split(":"))

    if x == a:
        w[t] += y-b
    elif y == b:
        w[t] += x-a
    a, b = x, y

print(*max(w.items(), key=lambda x: (x[1])))
