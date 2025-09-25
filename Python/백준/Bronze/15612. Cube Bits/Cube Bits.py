import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = []

    while n >= 3:
        m = n % 3
        n //= 3
        a.append(str(m))
    m = n % 3
    a.append(str(m))
    print(*a[::-1], sep="")
