import sys

input = sys.stdin.readline

for t in range(int(input())):
    b, d = input().strip().split()
    print(sum(map(int, [*d])) % (int(b)-1))
