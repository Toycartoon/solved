import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r = list(map(int, input().split()))

a = [[] for _ in range(m)]
for i in range(n):
    x, *k = map(int, input().split())
    for v in k:
        a[v-1].append(i+1)

for q in range(int(input())):
    i = int(input())
    print(*sorted(a[i-1], key=lambda x: r[x-1]) if len(a[i-1]) > 0 else [-1])
