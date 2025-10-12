r, c = map(int, input().split())
g = [[*input()] for _ in range(r)]

pos = [float('inf') for _ in range(9)]
for i in range(c):
    for v in list(zip(*g))[i]:
        if v.isdigit():
            if pos[int(v)-1] == float('inf'):
                pos[int(v)-1] = i
s = sorted(list(set(pos)), reverse=True)
for i in pos:
    print(s.index(i)+1)
