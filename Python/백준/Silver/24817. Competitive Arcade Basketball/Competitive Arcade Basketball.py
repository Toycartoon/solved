import sys

input = sys.stdin.readline

w = {}
n, p, m = map(int, input().split())
for i in range(n):
    s = input().strip()
    w[s] = 0

for i in range(m):
    name, v = input().strip().split()
    w[name] += int(v)

ans = []
for i in w.keys():
    if w[i] >= p:
        ans.append(i)

if len(ans) > 0:
    for i in ans:
        print(f"{i} wins!")
else:
    print("No winner!")
