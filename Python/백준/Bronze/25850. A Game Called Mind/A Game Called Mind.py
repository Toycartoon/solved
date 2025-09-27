n = int(input())
a = []
for i in range(n):
    m, *v = map(int, input().split())
    for j in v:
        a.append((j, i))

a.sort()
for _, idx in a:
    print(chr(65+idx), end="")
