import sys

input = sys.stdin.readline

a = []
n, q = map(int, input().split())
for i in range(n):
    v = int(input())
    for _ in range(v):
        a.append(i+1)

for i in range(q):
    m = int(input())
    print(a[m])
