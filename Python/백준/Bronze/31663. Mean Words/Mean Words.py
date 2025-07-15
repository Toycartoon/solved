g = [[] for _ in range(45)]

for n in range(int(input())):
    s = input()
    for i in range(len(s)):
        g[i].append(ord(s[i]))

for i in g:
    if not i:
        break

    print(chr(sum(i) // len(i)), end="")
