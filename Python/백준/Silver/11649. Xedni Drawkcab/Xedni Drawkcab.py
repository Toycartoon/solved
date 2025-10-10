a = []
for t in range(int(input())):
    a.append(input()[::-1])

a.sort()
for i in a:
    print(i)
