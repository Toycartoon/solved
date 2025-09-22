import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(2025 * 10 ** (n-4))
    else:
        print(42025 * 10 ** (n-5))
