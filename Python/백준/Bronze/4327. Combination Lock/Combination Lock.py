from collections import deque

while True:
    n, t1, t2, t3 = map(int, input().split())
    if n == t1 == t2 == t3 == 0:
        break

    q = deque([i for i in range(40)])
    ans = 1080
    while q[0] != n:
        q.rotate(1)

    while q[0] != t1:
        q.rotate(1)
        ans += 9

    while q[0] != t2:
        q.rotate(-1)
        ans += 9

    while q[0] != t3:
        q.rotate(1)
        ans += 9

    print(ans)
