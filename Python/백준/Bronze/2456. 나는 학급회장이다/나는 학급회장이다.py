a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(int(input())):
    s = list(map(int, input().split()))
    for x in range(3):
        a[x][0] += s[x]
        a[x][s[x]] += 1

if a.count(max(a)) != 1:
    print(0, max(a)[0])
else:
    print(a.index(max(a))+1, max(a)[0])
