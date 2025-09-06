a, p = map(int, input().split())
d = [a]
while True:
    x = 0
    for i in str(d[-1]):
        x += int(i) ** p

    if x in d:
        print(len(d[:d.index(x)]))
        break
    else:
        d.append(x)
