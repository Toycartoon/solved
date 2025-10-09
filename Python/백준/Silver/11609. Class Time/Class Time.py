a = []
for t in range(int(input())):
    a.append(input().split())

a.sort(key=lambda x: (x[1], x[0]))
for i in a:
    print(*i)
