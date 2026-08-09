def solution(edges):
    node = [[0, 0] for _ in range(1000001)]     # in, out
    gen, dount, stick, eight = -1, 0, 0, 0
    cnt = 0
    
    for a, b in edges:
        node[a][1] += 1
        node[b][0] += 1
    
    for i in range(1000001):
        if node[i][0] == 0 and node[i][1] >= 2:
            gen = i
            cnt = node[i][1]
        elif node[i][0] >= 1 and node[i][1] == 0:
            stick += 1
        elif node[i][0] >= 2 and node[i][1] >= 2:
            eight += 1
    
    dount = cnt - (eight + stick)
    return (gen, dount, stick, eight)
