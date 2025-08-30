import sys

input = sys.stdin.readline

for q in range(int(input())):
    a, b = map(int, input().split())
    print(int(b % a == 0 and a < b))
