import sys

input = sys.stdin.readline

for t in range(int(input())):
    a, b = map(int, input().split())
    if b % a == 0:
        print("TAK")
    else:
        print("NIE")
