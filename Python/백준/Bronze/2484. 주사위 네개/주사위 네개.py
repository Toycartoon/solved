a = []
for i in range(int(input())):
    n = list(map(int, input().split()))
    n.sort()
    if n[0] == n[1] == n[2] == n[3]:
        a.append(50000 + n[0] * 5000)
    elif n[0] == n[1] == n[2] or n[1] == n[2] == n[3]:
        a.append(10000 + n[1] * 1000)
    elif n[0] == n[1] and n[2] == n[3]:
        a.append(2000 + n[0] * 500 + n[2] * 500)
    elif n[0] == n[1] or n[1] == n[2]:
        a.append(1000 + n[1] * 100)
    elif n[2] == n[3]:
        a.append(1000 + n[2] * 100)
    else:
        a.append(max(n) * 100)

print(max(a))
