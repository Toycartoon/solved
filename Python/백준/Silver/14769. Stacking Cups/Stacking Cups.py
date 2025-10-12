g = []
for t in range(int(input())):
    a, b = input().split()
    if b.isalpha():
        g.append((int(a)//2, b))
    else:
        g.append((int(b), a))
g.sort()
for i in g:
    print(i[1])
