a = []
for i in range(int(input())):
    w, h = map(int, input().split())
    a.append(((w ** 2 + h ** 2) ** 0.5 / 77, i+1))

a.sort(key=lambda x: (-x[0], x[1]))
for i in a:
    print(i[1])
