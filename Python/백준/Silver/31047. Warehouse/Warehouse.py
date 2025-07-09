import sys

input = sys.stdin.readline

for t in range(int(input())):
    a = {}
    for n in range(int(input())):
        s, c = input().split()

        if s in a:
            a[s] += int(c)
        else:
            a[s] = int(c)

    print(len(a))
    for i in sorted(a.items(), key=lambda x: (-x[1], x[0])):
        print(*i)
