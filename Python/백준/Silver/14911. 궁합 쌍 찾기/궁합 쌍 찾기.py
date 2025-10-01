a = list(map(int, input().split()))
n = int(input())

ans = set()
s = set()
for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            continue
        if a[i] + a[j] == n and (min(i, j), max(i, j)) not in s:
            s.add((min(i, j), max(i, j)))
            ans.add((min(a[i], a[j]), max(a[i], a[j])))

ans = sorted(list(ans))
for i in ans:
    print(*i)
print(len(ans))
