a = []
n = int(input())
for i in range(3):
    a.append(list(map(int, input().split())))

v = []
for i in zip(*a):
    v.append(sorted(i)[1])
print(*v)
