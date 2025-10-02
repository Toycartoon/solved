a = []
for _ in range(int(input())):
    k = input()
    if len({*k}) == 1:
        a.append(int(k))
        continue

    f = True
    for i in range(1, len(k)):
        if k[i-1] >= k[i]:
            f = False
            break
    if f:
        a.append(int(k))
print(min(a) if len(a) > 0 else "NERASTA")
