import sys

input = sys.stdin.readline

for t in range(int(input())):
    m, n = map(int, input().split())
    a = input().strip().split()

    q = []
    inq = set()
    for i in range(n):
        s, e = map(int, input().split())
        inq.add(s)
        q.append((s, e))

    q.sort(key=lambda x: x[1])
    qidx = 0
    idx = 0
    ans = []
    for i in range(m):
        if len(q) > qidx and q[qidx][1]-1 == i:
            ans.append(a[q[qidx][0]-1])
            qidx += 1
        else:
            for x in range(idx, m):
                if x+1 not in inq:
                    idx = x+1
                    ans.append(a[x])
                    break

    print(*ans)
