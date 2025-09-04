import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    print(pow(2, n-2, 1000000007) if n > 1 else 1)
