arr = []
for i in range(int(input())):
    a, b, g = map(int, input().split())
    arr.append((a, b, g))

ans = 0
for i in range(3):
    v = [False for _ in range(3)]
    v[i] = True

    s = 0
    for a, b, g in arr:
        v[a-1], v[b-1] = v[b-1], v[a-1]
        if v[g-1]:
            s += 1
    ans = max(ans, s)
print(ans)
