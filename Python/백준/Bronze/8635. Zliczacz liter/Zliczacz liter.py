w = {}
for i in range(int(input())):
    s = input()
    for x in s:
        if x == " ":
            continue
        if x in w:
            w[x] += 1
        else:
            w[x] = 1

for i in sorted(w.items(), key=lambda x: (-int(97 <= ord(x[0]) <= 122), x[0])):
    print(*i)
