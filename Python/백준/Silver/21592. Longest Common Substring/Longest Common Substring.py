w = {}
a = []
for i in range(int(input())):
    a.append(input())
a.sort(key=len)

for i in range(len(a[0]), -1, -1):
    for j in range(i, len(a[0])+1):
        f = True
        s = a[0][j-i:j]
        for k in a:
            if s not in k:
                f = False
                break
        if f:
            print(i)
            exit()
