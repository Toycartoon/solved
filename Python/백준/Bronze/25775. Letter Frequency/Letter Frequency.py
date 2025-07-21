w = {}
for i in range(int(input())):
    s = input()
    for v in range(len(s)):
        if v+1 in w:
            if s[v] in w[v+1]:
                w[v+1][s[v]] += 1
            else:
                w[v+1][s[v]] = 1
        else:
            w[v+1] = {s[v]: 1}

for i in sorted(w.keys()):
    mx = max(w[i].values())
    print(f"{i}: ", end="")

    for v in sorted(w[i].keys()):
        if w[i][v] == mx:
            print(v, end=" ")
    print()
