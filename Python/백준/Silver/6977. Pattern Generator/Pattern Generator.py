from itertools import combinations as comb
import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())
    print("The bit patterns are")
    for i in comb(range(n), k):
        a = [0 for _ in range(n)]
        for v in i:
            a[v] = 1
        print(*a, sep="")
    print()
