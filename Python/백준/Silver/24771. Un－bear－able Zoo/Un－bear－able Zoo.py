import sys

input = sys.stdin.readline

t = 1
while True:
    n = int(input())

    if n == 0:
        break

    a = {}
    for i in range(n):
        s = input().strip().split()

        if s[-1].lower() not in a:
            a[s[-1].lower()] = 1
        else:
            a[s[-1].lower()] += 1

    print(f"List {t}:")
    for v in sorted(a.keys()):
        print(f"{v} | {a[v]}")

    t += 1
