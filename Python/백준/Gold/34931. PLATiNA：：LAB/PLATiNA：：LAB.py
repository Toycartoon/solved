t, n = map(int, input().split())
s = input()

div = []
l = [s[0]]
for i in range(1, t):
    if s[i-1] != s[i]:
        l.append(s[i])
    else:
        div.append(l)
        l = [s[i]]
div.append(l)

for i in div:
    if len(i) % 2 == 0:
        for k in range(1, len(i) // 2):
            if k <= n:
                i[k], i[-k-1] = i[k-1], i[-k]
            else:
                if i[k-1] == "A":
                    i[k] = "B"
                    i[-k-1] = "A"
                else:
                    i[k] = "A"
                    i[-k-1] = "B"
    else:
        for k in range(1, len(i) // 2+1):
            if k <= n:
                i[k] = i[0]
                i[-k-1] = i[-1]
            else:
                if i[k-1] == "A":
                    i[k] = "B"
                    i[-k-1] = "B"
                else:
                    i[k] = "A"
                    i[-k-1] = "A"
    print(*i, sep="", end="")
