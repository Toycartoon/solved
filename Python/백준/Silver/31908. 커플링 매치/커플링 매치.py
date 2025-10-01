w = {}
for i in range(int(input())):
    a, b = input().split()
    if b == "-":
        continue

    if b in w:
        w[b].append(a)
    else:
        w[b] = [a]

ans = []
for i in w.values():
    if len(i) == 2:
        ans.append(i)

print(len(ans))
for i in ans:
    print(*i)
