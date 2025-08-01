a, b = map(int, input().split())
c, d = map(int, input().split())

ans = [False for _ in range(101)]
for i in range(a, b):
    ans[i] = True

for i in range(c, d):
    ans[i] = True

print(ans.count(True))
