from itertools import combinations as comb
import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    f = True
    for i, j, k in comb(range(n), 3):
        if a[i] - a[j] == a[j] - a[k]:
            f = False
            break
    print(f"Case #{t+1}: {'YES' if f else 'NO'}")
