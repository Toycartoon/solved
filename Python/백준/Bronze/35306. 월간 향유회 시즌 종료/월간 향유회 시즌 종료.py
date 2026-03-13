import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ans = set()
a = [list(map(int, input().split())) for _ in range(n)]
a = list(zip(*a))

for i in range(k):
    if a[i].count(max(a[i])) == 1:
        ans.add(a[i].index(max(a[i])))
print(len(ans))
