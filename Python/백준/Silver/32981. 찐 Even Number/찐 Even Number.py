import sys

input = sys.stdin.readline

for q in range(int(input())):
    n = int(input())
    print((4 * pow(5, n-1, 1000000007)) % 1000000007 if n != 1 else 5)
