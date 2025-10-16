n, m = map(int, input().split())
q = []
for _ in range(n):
    com, *nt = input().split()
    if com == "order":
        q.append((int(nt[0]), int(nt[1])))
    elif com == "complete":
        for i in range(len(q)):
            if q[i][0] == int(nt[0]):
                q.pop(i)
                break
    elif com == "sort":
        q.sort(key=lambda x: (x[1], x[0]))

    if len(q) == 0:
        print("sleep")
    else:
        for i in q:
            print(i[0], end=' ')
        print()
