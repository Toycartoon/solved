import sys

input = sys.stdin.readline

for t in range(int(input())):
    _ = input()
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s.sort(reverse=True)
    b.sort(reverse=True)
    while s and b:
        if s[-1] < b[-1]:
            s.pop()
        else:
            b.pop()

    if len(s) == 0:
        print("B")
    elif len(b) == 0:
        print("S")
    else:
        print("C")
