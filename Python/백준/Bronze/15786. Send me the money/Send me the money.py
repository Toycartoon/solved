n, m = map(int, input().split())
p = input()
for _ in range(m):
    s = input()
    idx = 0
    for i in s:
        if i == p[idx]:
            idx += 1
            if idx == n:
                break

    print(str(idx == n).lower())
