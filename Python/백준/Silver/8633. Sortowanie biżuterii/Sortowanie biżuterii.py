a = []
for i in range(int(input())):
    a.append(input())

a = sorted(sorted(a), key=len)
for i in a:
    print(i)
