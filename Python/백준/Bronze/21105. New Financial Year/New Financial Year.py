import sys

input = sys.stdin.readline

for i in range(int(input())):
    p, c = map(float, input().split())
    print((100 * p) / (100 + c))
