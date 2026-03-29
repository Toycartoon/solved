import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())
    
    if n == 1:
        print(1)
    elif k != 2:
        print(-1)
    else:
        print(*range(2, n+1), 1)
