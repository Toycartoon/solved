import sys

input = sys.stdin.readline

def dolmen(a, b):
    return ((a + b) * (a + b - 1) // 2) * (a + b)

for t in range(int(input())):
    a, b = map(int, input().split())
    print(dolmen(a, b))
