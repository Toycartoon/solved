n = int(input())
a = [0 for _ in range(n+1)]

v = []
for i in range(n):
    x, y, z = map(int, input().split())
    v.append((x, y, z))

v.sort(key=lambda x: -x[2])
cnt = 0
for x, y, z in v:
    if a[x] < 2:
        print(x, y)
        a[x] += 1
        cnt += 1

        if cnt == 3:
            break
