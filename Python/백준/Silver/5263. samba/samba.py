import sys

input = sys.stdin.readline

w = {}
n, m = map(int, input().split())
for i in range(n):
    s = input().strip()
    if s in w:
        w[s] += 1
    else:
        w[s] = 1

for i in w.keys():
    if w[i] % m != 0:
        print(i)
