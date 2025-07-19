import sys

input = sys.stdin.readline

a = set()
while True:
    try:
        d, *s = input().strip().split()
        a.add(" ".join(s))
    except ValueError:
        break

print(len(a))
