import sys

input = sys.stdin.readline

a = []
n, m = map(int, input().split())
for i in range(m):
    a.append(int(input()))

if n == 2 and len(set(a)) == 2:
    print(-1)
elif n == 2 and a[0] == 0:
    print(1)
    print(1, -1, 1)
    print(1, 3, 4)
    for i in range(m):
        print(2, 1, 2)
else:
    print(1)
    print(1, -1, 1)
    print(1, 0, 2)
    for i in range(n-2):
        print(1, i+3, i+4)

    for i in a:
        if i == 1:
            print(2, 1, 2)
        else:
            print(2, 1, 3)
